# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AlertRuleResource
    from ._models_py3 import AlertRuleResourceCollection
    from ._models_py3 import AlertRuleResourcePatch
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Incident
    from ._models_py3 import IncidentListResult
    from ._models_py3 import LocalizableString
    from ._models_py3 import LocationThresholdRuleCondition
    from ._models_py3 import LogProfileCollection
    from ._models_py3 import LogProfileResource
    from ._models_py3 import LogProfileResourcePatch
    from ._models_py3 import ManagementEventAggregationCondition
    from ._models_py3 import ManagementEventRuleCondition
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricDefinition
    from ._models_py3 import MetricDefinitionCollection
    from ._models_py3 import Resource
    from ._models_py3 import RetentionPolicy
    from ._models_py3 import RuleAction
    from ._models_py3 import RuleCondition
    from ._models_py3 import RuleDataSource
    from ._models_py3 import RuleEmailAction
    from ._models_py3 import RuleManagementEventClaimsDataSource
    from ._models_py3 import RuleManagementEventDataSource
    from ._models_py3 import RuleMetricDataSource
    from ._models_py3 import RuleWebhookAction
    from ._models_py3 import ThresholdRuleCondition
except (SyntaxError, ImportError):
    from ._models import AlertRuleResource  # type: ignore
    from ._models import AlertRuleResourceCollection  # type: ignore
    from ._models import AlertRuleResourcePatch  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Incident  # type: ignore
    from ._models import IncidentListResult  # type: ignore
    from ._models import LocalizableString  # type: ignore
    from ._models import LocationThresholdRuleCondition  # type: ignore
    from ._models import LogProfileCollection  # type: ignore
    from ._models import LogProfileResource  # type: ignore
    from ._models import LogProfileResourcePatch  # type: ignore
    from ._models import ManagementEventAggregationCondition  # type: ignore
    from ._models import ManagementEventRuleCondition  # type: ignore
    from ._models import MetricAvailability  # type: ignore
    from ._models import MetricDefinition  # type: ignore
    from ._models import MetricDefinitionCollection  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RetentionPolicy  # type: ignore
    from ._models import RuleAction  # type: ignore
    from ._models import RuleCondition  # type: ignore
    from ._models import RuleDataSource  # type: ignore
    from ._models import RuleEmailAction  # type: ignore
    from ._models import RuleManagementEventClaimsDataSource  # type: ignore
    from ._models import RuleManagementEventDataSource  # type: ignore
    from ._models import RuleMetricDataSource  # type: ignore
    from ._models import RuleWebhookAction  # type: ignore
    from ._models import ThresholdRuleCondition  # type: ignore

from ._monitor_management_client_enums import (
    AggregationType,
    ConditionOperator,
    TimeAggregationOperator,
    Unit,
)

__all__ = [
    'AlertRuleResource',
    'AlertRuleResourceCollection',
    'AlertRuleResourcePatch',
    'ErrorResponse',
    'Incident',
    'IncidentListResult',
    'LocalizableString',
    'LocationThresholdRuleCondition',
    'LogProfileCollection',
    'LogProfileResource',
    'LogProfileResourcePatch',
    'ManagementEventAggregationCondition',
    'ManagementEventRuleCondition',
    'MetricAvailability',
    'MetricDefinition',
    'MetricDefinitionCollection',
    'Resource',
    'RetentionPolicy',
    'RuleAction',
    'RuleCondition',
    'RuleDataSource',
    'RuleEmailAction',
    'RuleManagementEventClaimsDataSource',
    'RuleManagementEventDataSource',
    'RuleMetricDataSource',
    'RuleWebhookAction',
    'ThresholdRuleCondition',
    'AggregationType',
    'ConditionOperator',
    'TimeAggregationOperator',
    'Unit',
]
