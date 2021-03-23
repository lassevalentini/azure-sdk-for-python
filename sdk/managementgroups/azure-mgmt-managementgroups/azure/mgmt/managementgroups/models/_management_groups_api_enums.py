# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Enum0(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    CHILDREN = "children"
    PATH = "path"

class Enum2(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ALLOWED_PARENTS = "AllowedParents"
    ALLOWED_CHILDREN = "AllowedChildren"
    PARENT_AND_FIRST_LEVEL_CHILDREN = "ParentAndFirstLevelChildren"
    PARENT_ONLY = "ParentOnly"
    CHILDREN_ONLY = "ChildrenOnly"

class Enum3(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    FULL_HIERARCHY = "FullHierarchy"
    GROUPS_ONLY = "GroupsOnly"
    SUBSCRIPTIONS_ONLY = "SubscriptionsOnly"
    AUDIT = "Audit"

class Enum5(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    CREATE = "create"
    DELETE = "delete"

class ManagementGroupChildType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of child resource.
    """

    MICROSOFT_MANAGEMENT_MANAGEMENT_GROUPS = "Microsoft.Management/managementGroups"
    _SUBSCRIPTIONS = "/subscriptions"

class Permissions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The users specific permissions to this item.
    """

    NOACCESS = "noaccess"
    VIEW = "view"
    EDIT = "edit"
    DELETE = "delete"

class Reason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Required if nameAvailable == false. Invalid indicates the name provided does not match the
    resource provider's naming requirements (incorrect length, unsupported characters, etc.)
    AlreadyExists indicates that the name is already in use and is therefore unavailable.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the Tenant Backfill
    """

    NOT_STARTED = "NotStarted"
    NOT_STARTED_BUT_GROUPS_EXIST = "NotStartedButGroupsExist"
    STARTED = "Started"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
