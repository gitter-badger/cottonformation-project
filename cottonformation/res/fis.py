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
class ExperimentTemplateExperimentTemplateStopCondition(Property):
    """
    AWS Object Type = "AWS::FIS::ExperimentTemplate.ExperimentTemplateStopCondition"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html

    Property Document:
    
    - ``rp_Source``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-source
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-value
    """
    AWS_OBJECT_TYPE = "AWS::FIS::ExperimentTemplate.ExperimentTemplateStopCondition"
    
    rp_Source: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Source"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-source"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html#cfn-fis-experimenttemplate-experimenttemplatestopcondition-value"""

@attr.s
class ExperimentTemplateExperimentTemplateAction(Property):
    """
    AWS Object Type = "AWS::FIS::ExperimentTemplate.ExperimentTemplateAction"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html

    Property Document:
    
    - ``rp_ActionId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-actionid
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-description
    - ``p_Parameters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-parameters
    - ``p_StartAfter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-startafter
    - ``p_Targets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-targets
    """
    AWS_OBJECT_TYPE = "AWS::FIS::ExperimentTemplate.ExperimentTemplateAction"
    
    rp_ActionId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ActionId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-actionid"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-description"""
    p_Parameters: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Parameters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-parameters"""
    p_StartAfter: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "StartAfter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-startafter"""
    p_Targets: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "Targets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html#cfn-fis-experimenttemplate-experimenttemplateaction-targets"""

@attr.s
class ExperimentTemplateExperimentTemplateTargetFilter(Property):
    """
    AWS Object Type = "AWS::FIS::ExperimentTemplate.ExperimentTemplateTargetFilter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html

    Property Document:
    
    - ``rp_Path``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-path
    - ``rp_Values``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-values
    """
    AWS_OBJECT_TYPE = "AWS::FIS::ExperimentTemplate.ExperimentTemplateTargetFilter"
    
    rp_Path: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Path"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-path"""
    rp_Values: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "Values"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html#cfn-fis-experimenttemplate-experimenttemplatetargetfilter-values"""

@attr.s
class ExperimentTemplateExperimentTemplateTarget(Property):
    """
    AWS Object Type = "AWS::FIS::ExperimentTemplate.ExperimentTemplateTarget"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html

    Property Document:
    
    - ``rp_ResourceType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetype
    - ``rp_SelectionMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-selectionmode
    - ``p_Filters``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-filters
    - ``p_ResourceArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcearns
    - ``p_ResourceTags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetags
    """
    AWS_OBJECT_TYPE = "AWS::FIS::ExperimentTemplate.ExperimentTemplateTarget"
    
    rp_ResourceType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetype"""
    rp_SelectionMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SelectionMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-selectionmode"""
    p_Filters: typing.List[typing.Union['ExperimentTemplateExperimentTemplateTargetFilter', dict]] = attr.ib(
        default=None,
        converter=ExperimentTemplateExperimentTemplateTargetFilter.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ExperimentTemplateExperimentTemplateTargetFilter), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Filters"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-filters"""
    p_ResourceArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcearns"""
    p_ResourceTags: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type))),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceTags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html#cfn-fis-experimenttemplate-experimenttemplatetarget-resourcetags"""


#--- Resource declaration ---

@attr.s
class ExperimentTemplate(Resource):
    """
    AWS Object Type = "AWS::FIS::ExperimentTemplate"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html

    Property Document:
    
    - ``rp_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-description
    - ``rp_RoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-rolearn
    - ``rp_StopConditions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-stopconditions
    - ``rp_Targets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-targets
    - ``p_Actions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-actions
    - ``rp_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-tags
    """
    AWS_OBJECT_TYPE = "AWS::FIS::ExperimentTemplate"

    
    rp_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-description"""
    rp_RoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "RoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-rolearn"""
    rp_StopConditions: typing.List[typing.Union['ExperimentTemplateExperimentTemplateStopCondition', dict]] = attr.ib(
        default=None,
        converter=ExperimentTemplateExperimentTemplateStopCondition.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ExperimentTemplateExperimentTemplateStopCondition), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "StopConditions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-stopconditions"""
    rp_Targets: typing.Union['ExperimentTemplateExperimentTemplateTarget', dict] = attr.ib(
        default=None,
        converter=ExperimentTemplateExperimentTemplateTarget.from_list,
        validator=attr.validators.instance_of(ExperimentTemplateExperimentTemplateTarget),
        metadata={AttrMeta.PROPERTY_NAME: "Targets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-targets"""
    p_Actions: typing.Union['ExperimentTemplateExperimentTemplateAction', dict] = attr.ib(
        default=None,
        converter=ExperimentTemplateExperimentTemplateAction.from_list,
        validator=attr.validators.optional(attr.validators.instance_of(ExperimentTemplateExperimentTemplateAction)),
        metadata={AttrMeta.PROPERTY_NAME: "Actions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-actions"""
    rp_Tags: typing.Dict[str, TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_mapping(key_validator=attr.validators.instance_of(str), value_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#cfn-fis-experimenttemplate-tags"""

    
    @property
    def rv_Id(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html#aws-resource-fis-experimenttemplate-return-values"""
        return GetAtt(resource=self, attr_name="Id")
    
