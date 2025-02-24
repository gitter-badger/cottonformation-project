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
class TaskFilterRule(Property):
    """
    AWS Object Type = "AWS::DataSync::Task.FilterRule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html

    Property Document:
    
    - ``p_FilterType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-filtertype
    - ``p_Value``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-value
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::Task.FilterRule"
    
    p_FilterType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "FilterType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-filtertype"""
    p_Value: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Value"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-filterrule.html#cfn-datasync-task-filterrule-value"""

@attr.s
class LocationS3S3Config(Property):
    """
    AWS Object Type = "AWS::DataSync::LocationS3.S3Config"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html

    Property Document:
    
    - ``rp_BucketAccessRoleArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html#cfn-datasync-locations3-s3config-bucketaccessrolearn
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationS3.S3Config"
    
    rp_BucketAccessRoleArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketAccessRoleArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locations3-s3config.html#cfn-datasync-locations3-s3config-bucketaccessrolearn"""

@attr.s
class LocationNFSOnPremConfig(Property):
    """
    AWS Object Type = "AWS::DataSync::LocationNFS.OnPremConfig"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html

    Property Document:
    
    - ``rp_AgentArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html#cfn-datasync-locationnfs-onpremconfig-agentarns
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationNFS.OnPremConfig"
    
    rp_AgentArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "AgentArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-onpremconfig.html#cfn-datasync-locationnfs-onpremconfig-agentarns"""

@attr.s
class LocationNFSMountOptions(Property):
    """
    AWS Object Type = "AWS::DataSync::LocationNFS.MountOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html

    Property Document:
    
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html#cfn-datasync-locationnfs-mountoptions-version
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationNFS.MountOptions"
    
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationnfs-mountoptions.html#cfn-datasync-locationnfs-mountoptions-version"""

@attr.s
class LocationEFSEc2Config(Property):
    """
    AWS Object Type = "AWS::DataSync::LocationEFS.Ec2Config"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html

    Property Document:
    
    - ``rp_SecurityGroupArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-securitygrouparns
    - ``rp_SubnetArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-subnetarn
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationEFS.Ec2Config"
    
    rp_SecurityGroupArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-securitygrouparns"""
    rp_SubnetArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationefs-ec2config.html#cfn-datasync-locationefs-ec2config-subnetarn"""

@attr.s
class TaskOptions(Property):
    """
    AWS Object Type = "AWS::DataSync::Task.Options"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html

    Property Document:
    
    - ``p_Atime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-atime
    - ``p_BytesPerSecond``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-bytespersecond
    - ``p_Gid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-gid
    - ``p_LogLevel``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-loglevel
    - ``p_Mtime``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-mtime
    - ``p_OverwriteMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-overwritemode
    - ``p_PosixPermissions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-posixpermissions
    - ``p_PreserveDeletedFiles``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedeletedfiles
    - ``p_PreserveDevices``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedevices
    - ``p_TaskQueueing``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-taskqueueing
    - ``p_TransferMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-transfermode
    - ``p_Uid``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-uid
    - ``p_VerifyMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-verifymode
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::Task.Options"
    
    p_Atime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Atime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-atime"""
    p_BytesPerSecond: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "BytesPerSecond"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-bytespersecond"""
    p_Gid: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Gid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-gid"""
    p_LogLevel: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogLevel"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-loglevel"""
    p_Mtime: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Mtime"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-mtime"""
    p_OverwriteMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OverwriteMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-overwritemode"""
    p_PosixPermissions: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PosixPermissions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-posixpermissions"""
    p_PreserveDeletedFiles: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PreserveDeletedFiles"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedeletedfiles"""
    p_PreserveDevices: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PreserveDevices"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-preservedevices"""
    p_TaskQueueing: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TaskQueueing"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-taskqueueing"""
    p_TransferMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "TransferMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-transfermode"""
    p_Uid: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Uid"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-uid"""
    p_VerifyMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VerifyMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-options.html#cfn-datasync-task-options-verifymode"""

@attr.s
class TaskTaskSchedule(Property):
    """
    AWS Object Type = "AWS::DataSync::Task.TaskSchedule"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html

    Property Document:
    
    - ``rp_ScheduleExpression``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html#cfn-datasync-task-taskschedule-scheduleexpression
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::Task.TaskSchedule"
    
    rp_ScheduleExpression: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ScheduleExpression"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-task-taskschedule.html#cfn-datasync-task-taskschedule-scheduleexpression"""

@attr.s
class LocationSMBMountOptions(Property):
    """
    AWS Object Type = "AWS::DataSync::LocationSMB.MountOptions"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html

    Property Document:
    
    - ``p_Version``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html#cfn-datasync-locationsmb-mountoptions-version
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationSMB.MountOptions"
    
    p_Version: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Version"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datasync-locationsmb-mountoptions.html#cfn-datasync-locationsmb-mountoptions-version"""


#--- Resource declaration ---

@attr.s
class LocationNFS(Resource):
    """
    AWS Object Type = "AWS::DataSync::LocationNFS"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html

    Property Document:
    
    - ``rp_OnPremConfig``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig
    - ``rp_ServerHostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname
    - ``rp_Subdirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory
    - ``p_MountOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationNFS"

    
    rp_OnPremConfig: typing.Union['LocationNFSOnPremConfig', dict] = attr.ib(
        default=None,
        converter=LocationNFSOnPremConfig.from_dict,
        validator=attr.validators.instance_of(LocationNFSOnPremConfig),
        metadata={AttrMeta.PROPERTY_NAME: "OnPremConfig"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig"""
    rp_ServerHostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServerHostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname"""
    rp_Subdirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Subdirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory"""
    p_MountOptions: typing.Union['LocationNFSMountOptions', dict] = attr.ib(
        default=None,
        converter=LocationNFSMountOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(LocationNFSMountOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "MountOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags"""

    
    @property
    def rv_LocationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#aws-resource-datasync-locationnfs-return-values"""
        return GetAtt(resource=self, attr_name="LocationArn")
    
    @property
    def rv_LocationUri(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#aws-resource-datasync-locationnfs-return-values"""
        return GetAtt(resource=self, attr_name="LocationUri")
    

@attr.s
class LocationFSxWindows(Resource):
    """
    AWS Object Type = "AWS::DataSync::LocationFSxWindows"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html

    Property Document:
    
    - ``rp_FsxFilesystemArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn
    - ``rp_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password
    - ``rp_SecurityGroupArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns
    - ``rp_User``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user
    - ``p_Domain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain
    - ``p_Subdirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationFSxWindows"

    
    rp_FsxFilesystemArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "FsxFilesystemArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-fsxfilesystemarn"""
    rp_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-password"""
    rp_SecurityGroupArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-securitygrouparns"""
    rp_User: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "User"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-user"""
    p_Domain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Domain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-domain"""
    p_Subdirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Subdirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-subdirectory"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#cfn-datasync-locationfsxwindows-tags"""

    
    @property
    def rv_LocationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#aws-resource-datasync-locationfsxwindows-return-values"""
        return GetAtt(resource=self, attr_name="LocationArn")
    
    @property
    def rv_LocationUri(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationfsxwindows.html#aws-resource-datasync-locationfsxwindows-return-values"""
        return GetAtt(resource=self, attr_name="LocationUri")
    

@attr.s
class LocationS3(Resource):
    """
    AWS Object Type = "AWS::DataSync::LocationS3"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html

    Property Document:
    
    - ``rp_S3BucketArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn
    - ``rp_S3Config``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config
    - ``p_S3StorageClass``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass
    - ``p_Subdirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationS3"

    
    rp_S3BucketArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "S3BucketArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3bucketarn"""
    rp_S3Config: typing.Union['LocationS3S3Config', dict] = attr.ib(
        default=None,
        converter=LocationS3S3Config.from_dict,
        validator=attr.validators.instance_of(LocationS3S3Config),
        metadata={AttrMeta.PROPERTY_NAME: "S3Config"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3config"""
    p_S3StorageClass: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "S3StorageClass"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-s3storageclass"""
    p_Subdirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Subdirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-subdirectory"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#cfn-datasync-locations3-tags"""

    
    @property
    def rv_LocationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#aws-resource-datasync-locations3-return-values"""
        return GetAtt(resource=self, attr_name="LocationArn")
    
    @property
    def rv_LocationUri(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locations3.html#aws-resource-datasync-locations3-return-values"""
        return GetAtt(resource=self, attr_name="LocationUri")
    

@attr.s
class Task(Resource):
    """
    AWS Object Type = "AWS::DataSync::Task"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html

    Property Document:
    
    - ``rp_DestinationLocationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-destinationlocationarn
    - ``rp_SourceLocationArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-sourcelocationarn
    - ``p_CloudWatchLogGroupArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-cloudwatchloggrouparn
    - ``p_Excludes``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-excludes
    - ``p_Name``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-name
    - ``p_Options``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-options
    - ``p_Schedule``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-schedule
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::Task"

    
    rp_DestinationLocationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DestinationLocationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-destinationlocationarn"""
    rp_SourceLocationArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SourceLocationArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-sourcelocationarn"""
    p_CloudWatchLogGroupArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "CloudWatchLogGroupArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-cloudwatchloggrouparn"""
    p_Excludes: typing.List[typing.Union['TaskFilterRule', dict]] = attr.ib(
        default=None,
        converter=TaskFilterRule.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TaskFilterRule), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Excludes"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-excludes"""
    p_Name: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Name"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-name"""
    p_Options: typing.Union['TaskOptions', dict] = attr.ib(
        default=None,
        converter=TaskOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(TaskOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "Options"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-options"""
    p_Schedule: typing.Union['TaskTaskSchedule', dict] = attr.ib(
        default=None,
        converter=TaskTaskSchedule.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(TaskTaskSchedule)),
        metadata={AttrMeta.PROPERTY_NAME: "Schedule"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-schedule"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#cfn-datasync-task-tags"""

    
    @property
    def rv_TaskArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#aws-resource-datasync-task-return-values"""
        return GetAtt(resource=self, attr_name="TaskArn")
    
    @property
    def rv_ErrorCode(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#aws-resource-datasync-task-return-values"""
        return GetAtt(resource=self, attr_name="ErrorCode")
    
    @property
    def rv_ErrorDetail(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#aws-resource-datasync-task-return-values"""
        return GetAtt(resource=self, attr_name="ErrorDetail")
    
    @property
    def rv_Status(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#aws-resource-datasync-task-return-values"""
        return GetAtt(resource=self, attr_name="Status")
    
    @property
    def rv_SourceNetworkInterfaceArns(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#aws-resource-datasync-task-return-values"""
        return GetAtt(resource=self, attr_name="SourceNetworkInterfaceArns")
    
    @property
    def rv_DestinationNetworkInterfaceArns(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-task.html#aws-resource-datasync-task-return-values"""
        return GetAtt(resource=self, attr_name="DestinationNetworkInterfaceArns")
    

@attr.s
class LocationObjectStorage(Resource):
    """
    AWS Object Type = "AWS::DataSync::LocationObjectStorage"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html

    Property Document:
    
    - ``rp_AgentArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-agentarns
    - ``rp_BucketName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-bucketname
    - ``rp_ServerHostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverhostname
    - ``p_AccessKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-accesskey
    - ``p_SecretKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-secretkey
    - ``p_ServerPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverport
    - ``p_ServerProtocol``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverprotocol
    - ``p_Subdirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-subdirectory
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationObjectStorage"

    
    rp_AgentArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "AgentArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-agentarns"""
    rp_BucketName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "BucketName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-bucketname"""
    rp_ServerHostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServerHostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverhostname"""
    p_AccessKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AccessKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-accesskey"""
    p_SecretKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "SecretKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-secretkey"""
    p_ServerPort: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        metadata={AttrMeta.PROPERTY_NAME: "ServerPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverport"""
    p_ServerProtocol: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ServerProtocol"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-serverprotocol"""
    p_Subdirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Subdirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-subdirectory"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#cfn-datasync-locationobjectstorage-tags"""

    
    @property
    def rv_LocationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#aws-resource-datasync-locationobjectstorage-return-values"""
        return GetAtt(resource=self, attr_name="LocationArn")
    
    @property
    def rv_LocationUri(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationobjectstorage.html#aws-resource-datasync-locationobjectstorage-return-values"""
        return GetAtt(resource=self, attr_name="LocationUri")
    

@attr.s
class Agent(Resource):
    """
    AWS Object Type = "AWS::DataSync::Agent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html

    Property Document:
    
    - ``rp_ActivationKey``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-activationkey
    - ``p_AgentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-agentname
    - ``p_SecurityGroupArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-securitygrouparns
    - ``p_SubnetArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-subnetarns
    - ``p_VpcEndpointId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-vpcendpointid
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::Agent"

    
    rp_ActivationKey: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ActivationKey"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-activationkey"""
    p_AgentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "AgentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-agentname"""
    p_SecurityGroupArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SecurityGroupArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-securitygrouparns"""
    p_SubnetArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SubnetArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-subnetarns"""
    p_VpcEndpointId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "VpcEndpointId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-vpcendpointid"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#cfn-datasync-agent-tags"""

    
    @property
    def rv_EndpointType(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#aws-resource-datasync-agent-return-values"""
        return GetAtt(resource=self, attr_name="EndpointType")
    
    @property
    def rv_AgentArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-agent.html#aws-resource-datasync-agent-return-values"""
        return GetAtt(resource=self, attr_name="AgentArn")
    

@attr.s
class LocationEFS(Resource):
    """
    AWS Object Type = "AWS::DataSync::LocationEFS"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html

    Property Document:
    
    - ``rp_Ec2Config``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-ec2config
    - ``rp_EfsFilesystemArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-efsfilesystemarn
    - ``p_Subdirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-subdirectory
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationEFS"

    
    rp_Ec2Config: typing.Union['LocationEFSEc2Config', dict] = attr.ib(
        default=None,
        converter=LocationEFSEc2Config.from_dict,
        validator=attr.validators.instance_of(LocationEFSEc2Config),
        metadata={AttrMeta.PROPERTY_NAME: "Ec2Config"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-ec2config"""
    rp_EfsFilesystemArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EfsFilesystemArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-efsfilesystemarn"""
    p_Subdirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Subdirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-subdirectory"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#cfn-datasync-locationefs-tags"""

    
    @property
    def rv_LocationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#aws-resource-datasync-locationefs-return-values"""
        return GetAtt(resource=self, attr_name="LocationArn")
    
    @property
    def rv_LocationUri(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationefs.html#aws-resource-datasync-locationefs-return-values"""
        return GetAtt(resource=self, attr_name="LocationUri")
    

@attr.s
class LocationSMB(Resource):
    """
    AWS Object Type = "AWS::DataSync::LocationSMB"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html

    Property Document:
    
    - ``rp_AgentArns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-agentarns
    - ``rp_Password``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-password
    - ``rp_ServerHostname``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-serverhostname
    - ``rp_Subdirectory``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-subdirectory
    - ``rp_User``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-user
    - ``p_Domain``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-domain
    - ``p_MountOptions``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-mountoptions
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-tags
    """
    AWS_OBJECT_TYPE = "AWS::DataSync::LocationSMB"

    
    rp_AgentArns: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "AgentArns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-agentarns"""
    rp_Password: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Password"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-password"""
    rp_ServerHostname: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ServerHostname"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-serverhostname"""
    rp_Subdirectory: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Subdirectory"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-subdirectory"""
    rp_User: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "User"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-user"""
    p_Domain: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Domain"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-domain"""
    p_MountOptions: typing.Union['LocationSMBMountOptions', dict] = attr.ib(
        default=None,
        converter=LocationSMBMountOptions.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(LocationSMBMountOptions)),
        metadata={AttrMeta.PROPERTY_NAME: "MountOptions"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-mountoptions"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#cfn-datasync-locationsmb-tags"""

    
    @property
    def rv_LocationArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#aws-resource-datasync-locationsmb-return-values"""
        return GetAtt(resource=self, attr_name="LocationArn")
    
    @property
    def rv_LocationUri(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationsmb.html#aws-resource-datasync-locationsmb-return-values"""
        return GetAtt(resource=self, attr_name="LocationUri")
    
