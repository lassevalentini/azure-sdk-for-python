# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.quantum.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.quantum.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~azure.mgmt.quantum.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class OfferingsListResult(msrest.serialization.Model):
    """The response of a list Providers operation.

    :param value: Result of a list Providers operation.
    :type value: list[~azure.mgmt.quantum.models.ProviderDescription]
    :param next_link: Link to the next set of results. Not empty if Value contains incomplete list
     of Providers.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ProviderDescription]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OfferingsListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class Operation(msrest.serialization.Model):
    """Operation provided by provider.

    :param name: Name of the operation.
    :type name: str
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    :param display: Properties of the operation.
    :type display: ~azure.mgmt.quantum.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_data_action = kwargs.get('is_data_action', None)
        self.display = kwargs.get('display', None)


class OperationDisplay(msrest.serialization.Model):
    """Properties of the operation.

    :param provider: Provider name.
    :type provider: str
    :param resource: Resource name.
    :type resource: str
    :param operation: Operation name.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationsList(msrest.serialization.Model):
    """Lists the operations available.

    All required parameters must be populated in order to send to Azure.

    :param next_link: Url to follow for getting next page of operations.
    :type next_link: str
    :param value: Required. Array of operations.
    :type value: list[~azure.mgmt.quantum.models.Operation]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationsList, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs['value']


class PricingDetail(msrest.serialization.Model):
    """Detailed pricing information for an sku.

    :param id: Unique id for this pricing information.
    :type id: str
    :param value: The unit cost of this sku.
    :type value: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PricingDetail, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.value = kwargs.get('value', None)


class PricingDimension(msrest.serialization.Model):
    """Information about pricing dimension.

    :param id: Unique id of this pricing dimension.
    :type id: str
    :param name: The display name of this pricing dimension.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PricingDimension, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)


class Provider(msrest.serialization.Model):
    """Information about a Provider. A Provider is an entity that offers Targets to run Azure Quantum Jobs.

    :param provider_id: Unique id of this provider.
    :type provider_id: str
    :param provider_sku: The sku associated with pricing information for this provider.
    :type provider_sku: str
    :param instance_uri: A Uri identifying the specific instance of this provider.
    :type instance_uri: str
    :param application_name: The provider's marketplace application display name.
    :type application_name: str
    :param provisioning_state: Provisioning status field. Possible values include: "Succeeded",
     "Launching", "Updating", "Deleting", "Deleted", "Failed".
    :type provisioning_state: str or ~azure.mgmt.quantum.models.Status
    :param resource_usage_id: Id to track resource usage for the provider.
    :type resource_usage_id: str
    """

    _attribute_map = {
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'provider_sku': {'key': 'providerSku', 'type': 'str'},
        'instance_uri': {'key': 'instanceUri', 'type': 'str'},
        'application_name': {'key': 'applicationName', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'resource_usage_id': {'key': 'resourceUsageId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Provider, self).__init__(**kwargs)
        self.provider_id = kwargs.get('provider_id', None)
        self.provider_sku = kwargs.get('provider_sku', None)
        self.instance_uri = kwargs.get('instance_uri', None)
        self.application_name = kwargs.get('application_name', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.resource_usage_id = kwargs.get('resource_usage_id', None)


class ProviderDescription(msrest.serialization.Model):
    """Information about an offering. A provider offering is an entity that offers Targets to run Azure Quantum Jobs.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param id: Unique provider's id.
    :type id: str
    :ivar name: Provider's display name.
    :vartype name: str
    :param properties: A list of provider-specific properties.
    :type properties: ~azure.mgmt.quantum.models.ProviderProperties
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ProviderProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProviderDescription, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = None
        self.properties = kwargs.get('properties', None)


class ProviderProperties(msrest.serialization.Model):
    """Provider properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar description: A description about this provider.
    :vartype description: str
    :ivar provider_type: Provider type.
    :vartype provider_type: str
    :ivar company: Company name.
    :vartype company: str
    :ivar default_endpoint: Provider's default endpoint.
    :vartype default_endpoint: str
    :param aad: Azure Active Directory info.
    :type aad: ~azure.mgmt.quantum.models.ProviderPropertiesAad
    :param managed_application: Provider's Managed-Application info.
    :type managed_application: ~azure.mgmt.quantum.models.ProviderPropertiesManagedApplication
    :param targets: The list of targets available from this provider.
    :type targets: list[~azure.mgmt.quantum.models.TargetDescription]
    :param skus: The list of skus available from this provider.
    :type skus: list[~azure.mgmt.quantum.models.SkuDescription]
    :param quota_dimensions: The list of quota dimensions from the provider.
    :type quota_dimensions: list[~azure.mgmt.quantum.models.QuotaDimension]
    :param pricing_dimensions: The list of pricing dimensions from the provider.
    :type pricing_dimensions: list[~azure.mgmt.quantum.models.PricingDimension]
    """

    _validation = {
        'description': {'readonly': True},
        'provider_type': {'readonly': True},
        'company': {'readonly': True},
        'default_endpoint': {'readonly': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'provider_type': {'key': 'providerType', 'type': 'str'},
        'company': {'key': 'company', 'type': 'str'},
        'default_endpoint': {'key': 'defaultEndpoint', 'type': 'str'},
        'aad': {'key': 'aad', 'type': 'ProviderPropertiesAad'},
        'managed_application': {'key': 'managedApplication', 'type': 'ProviderPropertiesManagedApplication'},
        'targets': {'key': 'targets', 'type': '[TargetDescription]'},
        'skus': {'key': 'skus', 'type': '[SkuDescription]'},
        'quota_dimensions': {'key': 'quotaDimensions', 'type': '[QuotaDimension]'},
        'pricing_dimensions': {'key': 'pricingDimensions', 'type': '[PricingDimension]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProviderProperties, self).__init__(**kwargs)
        self.description = None
        self.provider_type = None
        self.company = None
        self.default_endpoint = None
        self.aad = kwargs.get('aad', None)
        self.managed_application = kwargs.get('managed_application', None)
        self.targets = kwargs.get('targets', None)
        self.skus = kwargs.get('skus', None)
        self.quota_dimensions = kwargs.get('quota_dimensions', None)
        self.pricing_dimensions = kwargs.get('pricing_dimensions', None)


class ProviderPropertiesAad(msrest.serialization.Model):
    """Azure Active Directory info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar application_id: Provider's application id.
    :vartype application_id: str
    :ivar tenant_id: Provider's tenant id.
    :vartype tenant_id: str
    """

    _validation = {
        'application_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProviderPropertiesAad, self).__init__(**kwargs)
        self.application_id = None
        self.tenant_id = None


class ProviderPropertiesManagedApplication(msrest.serialization.Model):
    """Provider's Managed-Application info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar publisher_id: Provider's publisher id.
    :vartype publisher_id: str
    :ivar offer_id: Provider's offer id.
    :vartype offer_id: str
    """

    _validation = {
        'publisher_id': {'readonly': True},
        'offer_id': {'readonly': True},
    }

    _attribute_map = {
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProviderPropertiesManagedApplication, self).__init__(**kwargs)
        self.publisher_id = None
        self.offer_id = None


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs['location']


class QuantumWorkspace(TrackedResource):
    """The resource proxy definition object for quantum workspace.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param identity: Managed Identity information.
    :type identity: ~azure.mgmt.quantum.models.QuantumWorkspaceIdentity
    :param providers: List of Providers selected for this Workspace.
    :type providers: list[~azure.mgmt.quantum.models.Provider]
    :ivar usable: Whether the current workspace is ready to accept Jobs. Possible values include:
     "Yes", "No", "Partial".
    :vartype usable: str or ~azure.mgmt.quantum.models.UsableStatus
    :ivar provisioning_state: Provisioning status field. Possible values include: "Succeeded",
     "ProviderLaunching", "ProviderUpdating", "ProviderDeleting", "ProviderProvisioning", "Failed".
    :vartype provisioning_state: str or ~azure.mgmt.quantum.models.ProvisioningStatus
    :param storage_account: ARM Resource Id of the storage account associated with this workspace.
    :type storage_account: str
    :ivar endpoint_uri: The URI of the workspace endpoint.
    :vartype endpoint_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'usable': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'endpoint_uri': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'QuantumWorkspaceIdentity'},
        'providers': {'key': 'properties.providers', 'type': '[Provider]'},
        'usable': {'key': 'properties.usable', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'str'},
        'endpoint_uri': {'key': 'properties.endpointUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuantumWorkspace, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.providers = kwargs.get('providers', None)
        self.usable = None
        self.provisioning_state = None
        self.storage_account = kwargs.get('storage_account', None)
        self.endpoint_uri = None


class QuantumWorkspaceIdentity(msrest.serialization.Model):
    """Managed Identity information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: "SystemAssigned", "None".
    :type type: str or ~azure.mgmt.quantum.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuantumWorkspaceIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class QuotaDimension(msrest.serialization.Model):
    """Information about a specific quota dimension.

    :param id: Unique id of this dimension.
    :type id: str
    :param scope: The scope of this quota dimension.
    :type scope: str
    :param period: The reset period of this quota dimension.
    :type period: str
    :param quota: The max limit of this dimension.
    :type quota: float
    :param name: The display name of this quota dimension.
    :type name: str
    :param description: A description about this quota dimension.
    :type description: str
    :param unit: The standard unit of measurement used for this quota dimension.
    :type unit: str
    :param unit_plural: The standard unit of measurement used for this quota dimension in plural
     form.
    :type unit_plural: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'period': {'key': 'period', 'type': 'str'},
        'quota': {'key': 'quota', 'type': 'float'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'unit_plural': {'key': 'unitPlural', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuotaDimension, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.scope = kwargs.get('scope', None)
        self.period = kwargs.get('period', None)
        self.quota = kwargs.get('quota', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.unit = kwargs.get('unit', None)
        self.unit_plural = kwargs.get('unit_plural', None)


class SkuDescription(msrest.serialization.Model):
    """Information about a specific sku.

    :param id: Unique sku id.
    :type id: str
    :param name: Display name of this sku.
    :type name: str
    :param description: Description about this sku.
    :type description: str
    :param targets: The list of targets available for this sku.
    :type targets: list[str]
    :param quota_dimensions: The list of quota dimensions for this sku.
    :type quota_dimensions: list[~azure.mgmt.quantum.models.QuotaDimension]
    :param pricing_details: The list of pricing details for the sku.
    :type pricing_details: list[~azure.mgmt.quantum.models.PricingDetail]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'quota_dimensions': {'key': 'quotaDimensions', 'type': '[QuotaDimension]'},
        'pricing_details': {'key': 'pricingDetails', 'type': '[PricingDetail]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SkuDescription, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.targets = kwargs.get('targets', None)
        self.quota_dimensions = kwargs.get('quota_dimensions', None)
        self.pricing_details = kwargs.get('pricing_details', None)


class TagsObject(msrest.serialization.Model):
    """Tags object for patch operations.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TagsObject, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class TargetDescription(msrest.serialization.Model):
    """Information about a Target. A target is the component that can process a specific type of Job.

    :param id: Unique target id.
    :type id: str
    :param name: Display name of this target.
    :type name: str
    :param description: A description about this target.
    :type description: str
    :param accepted_data_formats: List of data formats accepted by this target.
    :type accepted_data_formats: list[str]
    :param accepted_content_encodings: List of content encodings accepted by this target.
    :type accepted_content_encodings: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'accepted_data_formats': {'key': 'acceptedDataFormats', 'type': '[str]'},
        'accepted_content_encodings': {'key': 'acceptedContentEncodings', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TargetDescription, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.accepted_data_formats = kwargs.get('accepted_data_formats', None)
        self.accepted_content_encodings = kwargs.get('accepted_content_encodings', None)


class WorkspaceListResult(msrest.serialization.Model):
    """The response of a list Workspaces operation.

    :param value: Result of a list Workspaces operation.
    :type value: list[~azure.mgmt.quantum.models.QuantumWorkspace]
    :param next_link: Link to the next set of results. Not empty if Value contains incomplete list
     of Workspaces.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[QuantumWorkspace]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(WorkspaceListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
