# -*- coding: utf-8 -*-

"""
This module
"""

import attr
import typing

from ..core.model import (
    Property, Resource, Tag, GetAtt, TypeHint, TypeCheck,
)
from ..core.constant import AttrMeta

#--- Property declaration ---

@attr.s
class IntegrationScheduledTriggerProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.ScheduledTriggerProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html

    Property Document:
    
    - ``rp_ScheduleExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression
    - ``p_DataPullMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode
    - ``p_FirstExecutionFrom``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom
    - ``p_ScheduleEndTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime
    - ``p_ScheduleOffset``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset
    - ``p_ScheduleStartTime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime
    - ``p_Timezone``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.ScheduledTriggerProperties"
    
    rp_ScheduleExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduleExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression"""
    p_DataPullMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DataPullMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode"""
    p_FirstExecutionFrom: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "FirstExecutionFrom"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom"""
    p_ScheduleEndTime: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduleEndTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime"""
    p_ScheduleOffset: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduleOffset"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset"""
    p_ScheduleStartTime: float = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(float)),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduleStartTime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime"""
    p_Timezone: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Timezone"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone"""

@attr.s
class IntegrationS3SourceProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.S3SourceProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html

    Property Document:
    
    - ``rp_BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketname
    - ``p_BucketPrefix``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketprefix
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.S3SourceProperties"
    
    rp_BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketname"""
    p_BucketPrefix: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "BucketPrefix"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketprefix"""

@attr.s
class ObjectTypeObjectTypeField(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::ObjectType.ObjectTypeField"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html

    Property Document:
    
    - ``p_ContentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-contenttype
    - ``p_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-source
    - ``p_Target``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-target
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::ObjectType.ObjectTypeField"
    
    p_ContentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ContentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-contenttype"""
    p_Source: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-source"""
    p_Target: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Target"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-target"""

@attr.s
class IntegrationIncrementalPullConfig(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.IncrementalPullConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html

    Property Document:
    
    - ``p_DatetimeTypeFieldName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html#cfn-customerprofiles-integration-incrementalpullconfig-datetimetypefieldname
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.IncrementalPullConfig"
    
    p_DatetimeTypeFieldName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DatetimeTypeFieldName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html#cfn-customerprofiles-integration-incrementalpullconfig-datetimetypefieldname"""

@attr.s
class IntegrationMarketoSourceProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.MarketoSourceProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html

    Property Document:
    
    - ``rp_Object``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html#cfn-customerprofiles-integration-marketosourceproperties-object
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.MarketoSourceProperties"
    
    rp_Object: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Object"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html#cfn-customerprofiles-integration-marketosourceproperties-object"""

@attr.s
class IntegrationTaskPropertiesMap(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.TaskPropertiesMap"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html

    Property Document:
    
    - ``rp_OperatorPropertyKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-operatorpropertykey
    - ``rp_Property``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-property
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.TaskPropertiesMap"
    
    rp_OperatorPropertyKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "OperatorPropertyKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-operatorpropertykey"""
    rp_Property: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Property"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-property"""

@attr.s
class IntegrationConnectorOperator(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.ConnectorOperator"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html

    Property Document:
    
    - ``p_Marketo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-marketo
    - ``p_S3``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-s3
    - ``p_Salesforce``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-salesforce
    - ``p_ServiceNow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-servicenow
    - ``p_Zendesk``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-zendesk
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.ConnectorOperator"
    
    p_Marketo: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Marketo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-marketo"""
    p_S3: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-s3"""
    p_Salesforce: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Salesforce"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-salesforce"""
    p_ServiceNow: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceNow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-servicenow"""
    p_Zendesk: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Zendesk"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-zendesk"""

@attr.s
class IntegrationZendeskSourceProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.ZendeskSourceProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html

    Property Document:
    
    - ``rp_Object``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html#cfn-customerprofiles-integration-zendesksourceproperties-object
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.ZendeskSourceProperties"
    
    rp_Object: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Object"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html#cfn-customerprofiles-integration-zendesksourceproperties-object"""

@attr.s
class IntegrationServiceNowSourceProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.ServiceNowSourceProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html

    Property Document:
    
    - ``rp_Object``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html#cfn-customerprofiles-integration-servicenowsourceproperties-object
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.ServiceNowSourceProperties"
    
    rp_Object: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Object"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html#cfn-customerprofiles-integration-servicenowsourceproperties-object"""

@attr.s
class IntegrationSalesforceSourceProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.SalesforceSourceProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html

    Property Document:
    
    - ``rp_Object``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-object
    - ``p_EnableDynamicFieldUpdate``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-enabledynamicfieldupdate
    - ``p_IncludeDeletedRecords``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-includedeletedrecords
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.SalesforceSourceProperties"
    
    rp_Object: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Object"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-object"""
    p_EnableDynamicFieldUpdate: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "EnableDynamicFieldUpdate"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-enabledynamicfieldupdate"""
    p_IncludeDeletedRecords: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "IncludeDeletedRecords"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-includedeletedrecords"""

@attr.s
class ObjectTypeObjectTypeKey(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::ObjectType.ObjectTypeKey"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html

    Property Document:
    
    - ``p_FieldNames``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-fieldnames
    - ``p_StandardIdentifiers``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::ObjectType.ObjectTypeKey"
    
    p_FieldNames: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "FieldNames"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-fieldnames"""
    p_StandardIdentifiers: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StandardIdentifiers"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers"""

@attr.s
class IntegrationTask(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.Task"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html

    Property Document:
    
    - ``rp_SourceFields``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-sourcefields
    - ``rp_TaskType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-tasktype
    - ``p_ConnectorOperator``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-connectoroperator
    - ``p_DestinationField``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-destinationfield
    - ``p_TaskProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-taskproperties
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.Task"
    
    rp_SourceFields: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SourceFields"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-sourcefields"""
    rp_TaskType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TaskType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-tasktype"""
    p_ConnectorOperator: typing.Union['IntegrationConnectorOperator', dict] = attr.ib(
        default=None,
        converter=IntegrationConnectorOperator.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationConnectorOperator)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorOperator"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-connectoroperator"""
    p_DestinationField: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationField"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-destinationfield"""
    p_TaskProperties: typing.List[typing.Union['IntegrationTaskPropertiesMap', dict]] = attr.ib(
        default=None,
        converter=IntegrationTaskPropertiesMap.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(IntegrationTaskPropertiesMap), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "TaskProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-taskproperties"""

@attr.s
class ObjectTypeKeyMap(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::ObjectType.KeyMap"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-name
    - ``p_ObjectTypeKeyList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-objecttypekeylist
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::ObjectType.KeyMap"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-name"""
    p_ObjectTypeKeyList: typing.List[typing.Union['ObjectTypeObjectTypeKey', dict]] = attr.ib(
        default=None,
        converter=ObjectTypeObjectTypeKey.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ObjectTypeObjectTypeKey), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectTypeKeyList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-objecttypekeylist"""

@attr.s
class IntegrationTriggerProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.TriggerProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html

    Property Document:
    
    - ``p_Scheduled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html#cfn-customerprofiles-integration-triggerproperties-scheduled
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.TriggerProperties"
    
    p_Scheduled: typing.Union['IntegrationScheduledTriggerProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationScheduledTriggerProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationScheduledTriggerProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "Scheduled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html#cfn-customerprofiles-integration-triggerproperties-scheduled"""

@attr.s
class ObjectTypeFieldMap(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::ObjectType.FieldMap"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html

    Property Document:
    
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-name
    - ``p_ObjectTypeField``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-objecttypefield
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::ObjectType.FieldMap"
    
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-name"""
    p_ObjectTypeField: typing.Union['ObjectTypeObjectTypeField', dict] = attr.ib(
        default=None,
        converter=ObjectTypeObjectTypeField.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ObjectTypeObjectTypeField)),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectTypeField"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-objecttypefield"""

@attr.s
class IntegrationSourceConnectorProperties(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.SourceConnectorProperties"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html

    Property Document:
    
    - ``p_Marketo``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-marketo
    - ``p_S3``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-s3
    - ``p_Salesforce``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce
    - ``p_ServiceNow``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow
    - ``p_Zendesk``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.SourceConnectorProperties"
    
    p_Marketo: typing.Union['IntegrationMarketoSourceProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationMarketoSourceProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationMarketoSourceProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "Marketo"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-marketo"""
    p_S3: typing.Union['IntegrationS3SourceProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationS3SourceProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationS3SourceProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "S3"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-s3"""
    p_Salesforce: typing.Union['IntegrationSalesforceSourceProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationSalesforceSourceProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationSalesforceSourceProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "Salesforce"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce"""
    p_ServiceNow: typing.Union['IntegrationServiceNowSourceProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationServiceNowSourceProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationServiceNowSourceProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "ServiceNow"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow"""
    p_Zendesk: typing.Union['IntegrationZendeskSourceProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationZendeskSourceProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationZendeskSourceProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "Zendesk"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk"""

@attr.s
class IntegrationTriggerConfig(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.TriggerConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html

    Property Document:
    
    - ``rp_TriggerType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggertype
    - ``p_TriggerProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggerproperties
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.TriggerConfig"
    
    rp_TriggerType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TriggerType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggertype"""
    p_TriggerProperties: typing.Union['IntegrationTriggerProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationTriggerProperties.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationTriggerProperties)),
        metadata={AttrMeta.PROPERTY_NAME: "TriggerProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggerproperties"""

@attr.s
class IntegrationSourceFlowConfig(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.SourceFlowConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html

    Property Document:
    
    - ``rp_ConnectorType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectortype
    - ``rp_SourceConnectorProperties``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties
    - ``p_ConnectorProfileName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename
    - ``p_IncrementalPullConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.SourceFlowConfig"
    
    rp_ConnectorType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectortype"""
    rp_SourceConnectorProperties: typing.Union['IntegrationSourceConnectorProperties', dict] = attr.ib(
        default=None,
        converter=IntegrationSourceConnectorProperties.from_dict,
        validator=attr.validators.instance_of(IntegrationSourceConnectorProperties),
        metadata={AttrMeta.PROPERTY_NAME: "SourceConnectorProperties"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties"""
    p_ConnectorProfileName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ConnectorProfileName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename"""
    p_IncrementalPullConfig: typing.Union['IntegrationIncrementalPullConfig', dict] = attr.ib(
        default=None,
        converter=IntegrationIncrementalPullConfig.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationIncrementalPullConfig)),
        metadata={AttrMeta.PROPERTY_NAME: "IncrementalPullConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig"""

@attr.s
class IntegrationFlowDefinition(Property):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration.FlowDefinition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html

    Property Document:
    
    - ``rp_FlowName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-flowname
    - ``rp_KmsArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-kmsarn
    - ``rp_SourceFlowConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig
    - ``rp_Tasks``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-tasks
    - ``rp_TriggerConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-triggerconfig
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-description
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration.FlowDefinition"
    
    rp_FlowName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FlowName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-flowname"""
    rp_KmsArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "KmsArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-kmsarn"""
    rp_SourceFlowConfig: typing.Union['IntegrationSourceFlowConfig', dict] = attr.ib(
        default=None,
        converter=IntegrationSourceFlowConfig.from_dict,
        validator=attr.validators.instance_of(IntegrationSourceFlowConfig),
        metadata={AttrMeta.PROPERTY_NAME: "SourceFlowConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig"""
    rp_Tasks: typing.List[typing.Union['IntegrationTask', dict]] = attr.ib(
        default=None,
        converter=IntegrationTask.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(IntegrationTask), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Tasks"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-tasks"""
    rp_TriggerConfig: typing.Union['IntegrationTriggerConfig', dict] = attr.ib(
        default=None,
        converter=IntegrationTriggerConfig.from_dict,
        validator=attr.validators.instance_of(IntegrationTriggerConfig),
        metadata={AttrMeta.PROPERTY_NAME: "TriggerConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-triggerconfig"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-description"""


#--- Resource declaration ---

@attr.s
class Domain(Resource):
    """
    AWS Object Type = "AWS::CustomerProfiles::Domain"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname
    - ``p_DeadLetterQueueUrl``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl
    - ``p_DefaultEncryptionKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey
    - ``p_DefaultExpirationDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Domain"

    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname"""
    p_DeadLetterQueueUrl: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DeadLetterQueueUrl"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl"""
    p_DefaultEncryptionKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultEncryptionKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey"""
    p_DefaultExpirationDays: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultExpirationDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags"""

    
    @property
    def rv_CreatedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#aws-resource-customerprofiles-domain-return-values"""
        return GetAtt(resource=self, attr_name="CreatedAt")
    
    @property
    def rv_LastUpdatedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#aws-resource-customerprofiles-domain-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedAt")
    

@attr.s
class Integration(Resource):
    """
    AWS Object Type = "AWS::CustomerProfiles::Integration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname
    - ``rp_ObjectTypeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename
    - ``p_FlowDefinition``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-flowdefinition
    - ``p_Uri``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::Integration"

    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname"""
    rp_ObjectTypeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectTypeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename"""
    p_FlowDefinition: typing.Union['IntegrationFlowDefinition', dict] = attr.ib(
        default=None,
        converter=IntegrationFlowDefinition.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(IntegrationFlowDefinition)),
        metadata={AttrMeta.PROPERTY_NAME: "FlowDefinition"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-flowdefinition"""
    p_Uri: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Uri"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags"""

    
    @property
    def rv_CreatedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#aws-resource-customerprofiles-integration-return-values"""
        return GetAtt(resource=self, attr_name="CreatedAt")
    
    @property
    def rv_LastUpdatedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#aws-resource-customerprofiles-integration-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedAt")
    

@attr.s
class ObjectType(Resource):
    """
    AWS Object Type = "AWS::CustomerProfiles::ObjectType"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html

    Property Document:
    
    - ``rp_DomainName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname
    - ``p_AllowProfileCreation``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description
    - ``p_EncryptionKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey
    - ``p_ExpirationDays``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays
    - ``p_Fields``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields
    - ``p_Keys``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys
    - ``p_ObjectTypeName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename
    - ``p_TemplateId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags
    """
    AWS_OBJECT_TYPE = "AWS::CustomerProfiles::ObjectType"

    
    rp_DomainName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DomainName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname"""
    p_AllowProfileCreation: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AllowProfileCreation"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description"""
    p_EncryptionKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "EncryptionKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey"""
    p_ExpirationDays: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ExpirationDays"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays"""
    p_Fields: typing.List[typing.Union['ObjectTypeFieldMap', dict]] = attr.ib(
        default=None,
        converter=ObjectTypeFieldMap.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ObjectTypeFieldMap), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Fields"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields"""
    p_Keys: typing.List[typing.Union['ObjectTypeKeyMap', dict]] = attr.ib(
        default=None,
        converter=ObjectTypeKeyMap.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ObjectTypeKeyMap), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Keys"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys"""
    p_ObjectTypeName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ObjectTypeName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename"""
    p_TemplateId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TemplateId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags"""

    
    @property
    def rv_CreatedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#aws-resource-customerprofiles-objecttype-return-values"""
        return GetAtt(resource=self, attr_name="CreatedAt")
    
    @property
    def rv_LastUpdatedAt(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#aws-resource-customerprofiles-objecttype-return-values"""
        return GetAtt(resource=self, attr_name="LastUpdatedAt")
    
