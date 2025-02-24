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
class ApplicationLogPattern(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.LogPattern"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html

    Property Document:
    
    - ``rp_Pattern``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-pattern
    - ``rp_PatternName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-patternname
    - ``rp_Rank``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-rank
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.LogPattern"
    
    rp_Pattern: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Pattern"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-pattern"""
    rp_PatternName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PatternName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-patternname"""
    rp_Rank: int = attr.ib(
        default=None,
        validator=attr.validators.instance_of(int),
        metadata={AttrMeta.PROPERTY_NAME: "Rank"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpattern.html#cfn-applicationinsights-application-logpattern-rank"""

@attr.s
class ApplicationLogPatternSet(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.LogPatternSet"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html

    Property Document:
    
    - ``rp_LogPatterns``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-logpatterns
    - ``rp_PatternSetName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-patternsetname
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.LogPatternSet"
    
    rp_LogPatterns: typing.List[typing.Union['ApplicationLogPattern', dict]] = attr.ib(
        default=None,
        converter=ApplicationLogPattern.from_list,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationLogPattern), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "LogPatterns"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-logpatterns"""
    rp_PatternSetName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PatternSetName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-logpatternset.html#cfn-applicationinsights-application-logpatternset-patternsetname"""

@attr.s
class ApplicationAlarm(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.Alarm"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html

    Property Document:
    
    - ``rp_AlarmName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-alarmname
    - ``p_Severity``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-severity
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.Alarm"
    
    rp_AlarmName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-alarmname"""
    p_Severity: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Severity"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarm.html#cfn-applicationinsights-application-alarm-severity"""

@attr.s
class ApplicationWindowsEvent(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.WindowsEvent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html

    Property Document:
    
    - ``rp_EventLevels``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventlevels
    - ``rp_EventName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventname
    - ``rp_LogGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-loggroupname
    - ``p_PatternSet``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-patternset
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.WindowsEvent"
    
    rp_EventLevels: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "EventLevels"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventlevels"""
    rp_EventName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "EventName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-eventname"""
    rp_LogGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-loggroupname"""
    p_PatternSet: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PatternSet"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-windowsevent.html#cfn-applicationinsights-application-windowsevent-patternset"""

@attr.s
class ApplicationCustomComponent(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.CustomComponent"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html

    Property Document:
    
    - ``rp_ComponentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-componentname
    - ``rp_ResourceList``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-resourcelist
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.CustomComponent"
    
    rp_ComponentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComponentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-componentname"""
    rp_ResourceList: typing.List[TypeHint.intrinsic_str] = attr.ib(
        default=None,
        validator=attr.validators.deep_iterable(member_validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type), iterable_validator=attr.validators.instance_of(list)),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceList"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-customcomponent.html#cfn-applicationinsights-application-customcomponent-resourcelist"""

@attr.s
class ApplicationJMXPrometheusExporter(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.JMXPrometheusExporter"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html

    Property Document:
    
    - ``p_HostPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-hostport
    - ``p_JMXURL``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-jmxurl
    - ``p_PrometheusPort``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-prometheusport
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.JMXPrometheusExporter"
    
    p_HostPort: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "HostPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-hostport"""
    p_JMXURL: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "JMXURL"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-jmxurl"""
    p_PrometheusPort: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PrometheusPort"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-jmxprometheusexporter.html#cfn-applicationinsights-application-jmxprometheusexporter-prometheusport"""

@attr.s
class ApplicationAlarmMetric(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.AlarmMetric"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html

    Property Document:
    
    - ``rp_AlarmMetricName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html#cfn-applicationinsights-application-alarmmetric-alarmmetricname
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.AlarmMetric"
    
    rp_AlarmMetricName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmMetricName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-alarmmetric.html#cfn-applicationinsights-application-alarmmetric-alarmmetricname"""

@attr.s
class ApplicationLog(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.Log"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html

    Property Document:
    
    - ``rp_LogType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logtype
    - ``p_Encoding``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-encoding
    - ``p_LogGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-loggroupname
    - ``p_LogPath``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logpath
    - ``p_PatternSet``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-patternset
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.Log"
    
    rp_LogType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "LogType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logtype"""
    p_Encoding: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Encoding"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-encoding"""
    p_LogGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-loggroupname"""
    p_LogPath: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "LogPath"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-logpath"""
    p_PatternSet: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PatternSet"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-log.html#cfn-applicationinsights-application-log-patternset"""

@attr.s
class ApplicationSubComponentConfigurationDetails(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.SubComponentConfigurationDetails"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html

    Property Document:
    
    - ``p_AlarmMetrics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics
    - ``p_Logs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-logs
    - ``p_WindowsEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.SubComponentConfigurationDetails"
    
    p_AlarmMetrics: typing.List[typing.Union['ApplicationAlarmMetric', dict]] = attr.ib(
        default=None,
        converter=ApplicationAlarmMetric.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationAlarmMetric), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmMetrics"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-alarmmetrics"""
    p_Logs: typing.List[typing.Union['ApplicationLog', dict]] = attr.ib(
        default=None,
        converter=ApplicationLog.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationLog), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Logs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-logs"""
    p_WindowsEvents: typing.List[typing.Union['ApplicationWindowsEvent', dict]] = attr.ib(
        default=None,
        converter=ApplicationWindowsEvent.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationWindowsEvent), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "WindowsEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponentconfigurationdetails.html#cfn-applicationinsights-application-subcomponentconfigurationdetails-windowsevents"""

@attr.s
class ApplicationConfigurationDetails(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.ConfigurationDetails"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html

    Property Document:
    
    - ``p_AlarmMetrics``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarmmetrics
    - ``p_Alarms``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarms
    - ``p_JMXPrometheusExporter``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter
    - ``p_Logs``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-logs
    - ``p_WindowsEvents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-windowsevents
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.ConfigurationDetails"
    
    p_AlarmMetrics: typing.List[typing.Union['ApplicationAlarmMetric', dict]] = attr.ib(
        default=None,
        converter=ApplicationAlarmMetric.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationAlarmMetric), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "AlarmMetrics"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarmmetrics"""
    p_Alarms: typing.List[typing.Union['ApplicationAlarm', dict]] = attr.ib(
        default=None,
        converter=ApplicationAlarm.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationAlarm), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Alarms"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-alarms"""
    p_JMXPrometheusExporter: typing.Union['ApplicationJMXPrometheusExporter', dict] = attr.ib(
        default=None,
        converter=ApplicationJMXPrometheusExporter.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationJMXPrometheusExporter)),
        metadata={AttrMeta.PROPERTY_NAME: "JMXPrometheusExporter"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-jmxprometheusexporter"""
    p_Logs: typing.List[typing.Union['ApplicationLog', dict]] = attr.ib(
        default=None,
        converter=ApplicationLog.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationLog), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Logs"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-logs"""
    p_WindowsEvents: typing.List[typing.Union['ApplicationWindowsEvent', dict]] = attr.ib(
        default=None,
        converter=ApplicationWindowsEvent.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationWindowsEvent), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "WindowsEvents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-configurationdetails.html#cfn-applicationinsights-application-configurationdetails-windowsevents"""

@attr.s
class ApplicationSubComponentTypeConfiguration(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.SubComponentTypeConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html

    Property Document:
    
    - ``rp_SubComponentConfigurationDetails``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponentconfigurationdetails
    - ``rp_SubComponentType``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponenttype
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.SubComponentTypeConfiguration"
    
    rp_SubComponentConfigurationDetails: typing.Union['ApplicationSubComponentConfigurationDetails', dict] = attr.ib(
        default=None,
        converter=ApplicationSubComponentConfigurationDetails.from_dict,
        validator=attr.validators.instance_of(ApplicationSubComponentConfigurationDetails),
        metadata={AttrMeta.PROPERTY_NAME: "SubComponentConfigurationDetails"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponentconfigurationdetails"""
    rp_SubComponentType: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "SubComponentType"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-subcomponenttypeconfiguration.html#cfn-applicationinsights-application-subcomponenttypeconfiguration-subcomponenttype"""

@attr.s
class ApplicationComponentConfiguration(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.ComponentConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html

    Property Document:
    
    - ``p_ConfigurationDetails``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-configurationdetails
    - ``p_SubComponentTypeConfigurations``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.ComponentConfiguration"
    
    p_ConfigurationDetails: typing.Union['ApplicationConfigurationDetails', dict] = attr.ib(
        default=None,
        converter=ApplicationConfigurationDetails.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationConfigurationDetails)),
        metadata={AttrMeta.PROPERTY_NAME: "ConfigurationDetails"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-configurationdetails"""
    p_SubComponentTypeConfigurations: typing.List[typing.Union['ApplicationSubComponentTypeConfiguration', dict]] = attr.ib(
        default=None,
        converter=ApplicationSubComponentTypeConfiguration.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationSubComponentTypeConfiguration), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "SubComponentTypeConfigurations"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentconfiguration.html#cfn-applicationinsights-application-componentconfiguration-subcomponenttypeconfigurations"""

@attr.s
class ApplicationComponentMonitoringSetting(Property):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application.ComponentMonitoringSetting"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html

    Property Document:
    
    - ``rp_ComponentConfigurationMode``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode
    - ``rp_Tier``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-tier
    - ``p_ComponentARN``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentarn
    - ``p_ComponentName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentname
    - ``p_CustomComponentConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration
    - ``p_DefaultOverwriteComponentConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application.ComponentMonitoringSetting"
    
    rp_ComponentConfigurationMode: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ComponentConfigurationMode"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentconfigurationmode"""
    rp_Tier: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Tier"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-tier"""
    p_ComponentARN: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ComponentARN"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentarn"""
    p_ComponentName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "ComponentName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-componentname"""
    p_CustomComponentConfiguration: typing.Union['ApplicationComponentConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationComponentConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationComponentConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "CustomComponentConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-customcomponentconfiguration"""
    p_DefaultOverwriteComponentConfiguration: typing.Union['ApplicationComponentConfiguration', dict] = attr.ib(
        default=None,
        converter=ApplicationComponentConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(ApplicationComponentConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DefaultOverwriteComponentConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationinsights-application-componentmonitoringsetting.html#cfn-applicationinsights-application-componentmonitoringsetting-defaultoverwritecomponentconfiguration"""


#--- Resource declaration ---

@attr.s
class Application(Resource):
    """
    AWS Object Type = "AWS::ApplicationInsights::Application"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html

    Property Document:
    
    - ``rp_ResourceGroupName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-resourcegroupname
    - ``p_AutoConfigurationEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-autoconfigurationenabled
    - ``p_CWEMonitorEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-cwemonitorenabled
    - ``p_ComponentMonitoringSettings``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-componentmonitoringsettings
    - ``p_CustomComponents``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-customcomponents
    - ``p_LogPatternSets``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-logpatternsets
    - ``p_OpsCenterEnabled``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opscenterenabled
    - ``p_OpsItemSNSTopicArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opsitemsnstopicarn
    - ``p_Tags``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-tags
    """
    AWS_OBJECT_TYPE = "AWS::ApplicationInsights::Application"

    
    rp_ResourceGroupName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ResourceGroupName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-resourcegroupname"""
    p_AutoConfigurationEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "AutoConfigurationEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-autoconfigurationenabled"""
    p_CWEMonitorEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "CWEMonitorEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-cwemonitorenabled"""
    p_ComponentMonitoringSettings: typing.List[typing.Union['ApplicationComponentMonitoringSetting', dict]] = attr.ib(
        default=None,
        converter=ApplicationComponentMonitoringSetting.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationComponentMonitoringSetting), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "ComponentMonitoringSettings"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-componentmonitoringsettings"""
    p_CustomComponents: typing.List[typing.Union['ApplicationCustomComponent', dict]] = attr.ib(
        default=None,
        converter=ApplicationCustomComponent.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationCustomComponent), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "CustomComponents"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-customcomponents"""
    p_LogPatternSets: typing.List[typing.Union['ApplicationLogPatternSet', dict]] = attr.ib(
        default=None,
        converter=ApplicationLogPatternSet.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(ApplicationLogPatternSet), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "LogPatternSets"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-logpatternsets"""
    p_OpsCenterEnabled: bool = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(bool)),
        metadata={AttrMeta.PROPERTY_NAME: "OpsCenterEnabled"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opscenterenabled"""
    p_OpsItemSNSTopicArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "OpsItemSNSTopicArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-opsitemsnstopicarn"""
    p_Tags: typing.List[typing.Union[Tag, dict]] = attr.ib(
        default=None,
        converter=Tag.from_list,
        validator=attr.validators.optional(attr.validators.deep_iterable(member_validator=attr.validators.instance_of(Tag), iterable_validator=attr.validators.instance_of(list))),
        metadata={AttrMeta.PROPERTY_NAME: "Tags"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#cfn-applicationinsights-application-tags"""

    
    @property
    def rv_ApplicationARN(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationinsights-application.html#aws-resource-applicationinsights-application-return-values"""
        return GetAtt(resource=self, attr_name="ApplicationARN")
    
