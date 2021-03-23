# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import TYPE_CHECKING

import msal

from .._internal import AadClient, AsyncContextManager
from .._internal.decorators import log_get_token_async
from ..._internal import validate_tenant_id
from ..._persistent_cache import _load_persistent_cache, TokenCachePersistenceOptions

if TYPE_CHECKING:
    from typing import Any
    from azure.core.credentials import AccessToken


class ClientSecretCredential(AsyncContextManager):
    """Authenticates as a service principal using a client ID and client secret.

    :param str tenant_id: ID of the service principal's tenant. Also called its 'directory' ID.
    :param str client_id: the service principal's client ID
    :param str client_secret: one of the service principal's client secrets

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example 'login.microsoftonline.com',
          the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
          defines authorities for other clouds.
    :keyword cache_persistence_options: configuration for persistent token caching. If unspecified, the credential
          will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    """

    def __init__(self, tenant_id, client_id, client_secret, **kwargs):
        # type: (str, str, str, **Any) -> None
        if not client_id:
            raise ValueError("client_id should be the id of an Azure Active Directory application")
        if not client_secret:
            raise ValueError("secret should be an Azure Active Directory application's client secret")
        if not tenant_id:
            raise ValueError(
                "tenant_id should be an Azure Active Directory tenant's id (also called its 'directory id')"
            )
        validate_tenant_id(tenant_id)

        cache_options = kwargs.pop("cache_persistence_options", None)
        if cache_options:
            cache = _load_persistent_cache(cache_options)
        else:
            cache = msal.TokenCache()

        self._client = AadClient(tenant_id, client_id, cache=cache, **kwargs)
        self._client_id = client_id
        self._secret = client_secret

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def close(self):
        """Close the credential's transport session."""

        await self._client.__aexit__()

    @log_get_token_async
    async def get_token(self, *scopes: str, **kwargs: "Any") -> "AccessToken":
        """Asynchronously request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
        :rtype: :class:`azure.core.credentials.AccessToken`
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
          attribute gives a reason. Any error response from Azure Active Directory is available as the error's
          ``response`` attribute.
        """
        if not scopes:
            raise ValueError("'get_token' requires at least one scope")

        token = self._client.get_cached_access_token(scopes, query={"client_id": self._client_id})
        if not token:
            token = await self._client.obtain_token_by_client_secret(scopes, self._secret, **kwargs)
        elif self._client.should_refresh(token):
            try:
                await self._client.obtain_token_by_client_secret(scopes, self._secret, **kwargs)
            except Exception:  # pylint: disable=broad-except
                pass
        return token
