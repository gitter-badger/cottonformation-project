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
class PlaceIndexDataSourceConfiguration(Property):
    """
    AWS Object Type = "AWS::Location::PlaceIndex.DataSourceConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html

    Property Document:
    
    - ``p_IntendedUse``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html#cfn-location-placeindex-datasourceconfiguration-intendeduse
    """
    AWS_OBJECT_TYPE = "AWS::Location::PlaceIndex.DataSourceConfiguration"
    
    p_IntendedUse: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "IntendedUse"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-placeindex-datasourceconfiguration.html#cfn-location-placeindex-datasourceconfiguration-intendeduse"""

@attr.s
class MapMapConfiguration(Property):
    """
    AWS Object Type = "AWS::Location::Map.MapConfiguration"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html

    Property Document:
    
    - ``rp_Style``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html#cfn-location-map-mapconfiguration-style
    """
    AWS_OBJECT_TYPE = "AWS::Location::Map.MapConfiguration"
    
    rp_Style: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "Style"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-location-map-mapconfiguration.html#cfn-location-map-mapconfiguration-style"""


#--- Resource declaration ---

@attr.s
class Tracker(Resource):
    """
    AWS Object Type = "AWS::Location::Tracker"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html

    Property Document:
    
    - ``rp_PricingPlan``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplan
    - ``rp_TrackerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-trackername
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-description
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-kmskeyid
    - ``p_PricingPlanDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplandatasource
    """
    AWS_OBJECT_TYPE = "AWS::Location::Tracker"

    
    rp_PricingPlan: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PricingPlan"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplan"""
    rp_TrackerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TrackerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-trackername"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-description"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-kmskeyid"""
    p_PricingPlanDataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PricingPlanDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#cfn-location-tracker-pricingplandatasource"""

    
    @property
    def rv_CreateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#aws-resource-location-tracker-return-values"""
        return GetAtt(resource=self, attr_name="CreateTime")
    
    @property
    def rv_TrackerArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#aws-resource-location-tracker-return-values"""
        return GetAtt(resource=self, attr_name="TrackerArn")
    
    @property
    def rv_UpdateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-tracker.html#aws-resource-location-tracker-return-values"""
        return GetAtt(resource=self, attr_name="UpdateTime")
    

@attr.s
class Map(Resource):
    """
    AWS Object Type = "AWS::Location::Map"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html

    Property Document:
    
    - ``rp_Configuration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-configuration
    - ``rp_MapName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-mapname
    - ``rp_PricingPlan``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-pricingplan
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-description
    """
    AWS_OBJECT_TYPE = "AWS::Location::Map"

    
    rp_Configuration: typing.Union['MapMapConfiguration', dict] = attr.ib(
        default=None,
        converter=MapMapConfiguration.from_dict,
        validator=attr.validators.instance_of(MapMapConfiguration),
        metadata={AttrMeta.PROPERTY_NAME: "Configuration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-configuration"""
    rp_MapName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "MapName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-mapname"""
    rp_PricingPlan: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PricingPlan"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-pricingplan"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#cfn-location-map-description"""

    
    @property
    def rv_CreateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#aws-resource-location-map-return-values"""
        return GetAtt(resource=self, attr_name="CreateTime")
    
    @property
    def rv_DataSource(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#aws-resource-location-map-return-values"""
        return GetAtt(resource=self, attr_name="DataSource")
    
    @property
    def rv_MapArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#aws-resource-location-map-return-values"""
        return GetAtt(resource=self, attr_name="MapArn")
    
    @property
    def rv_UpdateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-map.html#aws-resource-location-map-return-values"""
        return GetAtt(resource=self, attr_name="UpdateTime")
    

@attr.s
class GeofenceCollection(Resource):
    """
    AWS Object Type = "AWS::Location::GeofenceCollection"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html

    Property Document:
    
    - ``rp_CollectionName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-collectionname
    - ``rp_PricingPlan``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplan
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-description
    - ``p_KmsKeyId``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-kmskeyid
    - ``p_PricingPlanDataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplandatasource
    """
    AWS_OBJECT_TYPE = "AWS::Location::GeofenceCollection"

    
    rp_CollectionName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CollectionName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-collectionname"""
    rp_PricingPlan: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PricingPlan"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplan"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-description"""
    p_KmsKeyId: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "KmsKeyId"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-kmskeyid"""
    p_PricingPlanDataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "PricingPlanDataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#cfn-location-geofencecollection-pricingplandatasource"""

    
    @property
    def rv_CollectionArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#aws-resource-location-geofencecollection-return-values"""
        return GetAtt(resource=self, attr_name="CollectionArn")
    
    @property
    def rv_CreateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#aws-resource-location-geofencecollection-return-values"""
        return GetAtt(resource=self, attr_name="CreateTime")
    
    @property
    def rv_UpdateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-geofencecollection.html#aws-resource-location-geofencecollection-return-values"""
        return GetAtt(resource=self, attr_name="UpdateTime")
    

@attr.s
class TrackerConsumer(Resource):
    """
    AWS Object Type = "AWS::Location::TrackerConsumer"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html

    Property Document:
    
    - ``rp_ConsumerArn``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-consumerarn
    - ``rp_TrackerName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-trackername
    """
    AWS_OBJECT_TYPE = "AWS::Location::TrackerConsumer"

    
    rp_ConsumerArn: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "ConsumerArn"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-consumerarn"""
    rp_TrackerName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "TrackerName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-trackerconsumer.html#cfn-location-trackerconsumer-trackername"""

    

@attr.s
class RouteCalculator(Resource):
    """
    AWS Object Type = "AWS::Location::RouteCalculator"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html

    Property Document:
    
    - ``rp_CalculatorName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname
    - ``rp_DataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource
    - ``rp_PricingPlan``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description
    """
    AWS_OBJECT_TYPE = "AWS::Location::RouteCalculator"

    
    rp_CalculatorName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "CalculatorName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname"""
    rp_DataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource"""
    rp_PricingPlan: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PricingPlan"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description"""

    
    @property
    def rv_CalculatorArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#aws-resource-location-routecalculator-return-values"""
        return GetAtt(resource=self, attr_name="CalculatorArn")
    
    @property
    def rv_CreateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#aws-resource-location-routecalculator-return-values"""
        return GetAtt(resource=self, attr_name="CreateTime")
    
    @property
    def rv_UpdateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#aws-resource-location-routecalculator-return-values"""
        return GetAtt(resource=self, attr_name="UpdateTime")
    

@attr.s
class PlaceIndex(Resource):
    """
    AWS Object Type = "AWS::Location::PlaceIndex"

    Resource Document: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html

    Property Document:
    
    - ``rp_DataSource``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasource
    - ``rp_IndexName``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-indexname
    - ``rp_PricingPlan``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-pricingplan
    - ``p_DataSourceConfiguration``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasourceconfiguration
    - ``p_Description``: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-description
    """
    AWS_OBJECT_TYPE = "AWS::Location::PlaceIndex"

    
    rp_DataSource: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "DataSource"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasource"""
    rp_IndexName: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "IndexName"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-indexname"""
    rp_PricingPlan: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.instance_of(TypeCheck.intrinsic_str_type),
        metadata={AttrMeta.PROPERTY_NAME: "PricingPlan"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-pricingplan"""
    p_DataSourceConfiguration: typing.Union['PlaceIndexDataSourceConfiguration', dict] = attr.ib(
        default=None,
        converter=PlaceIndexDataSourceConfiguration.from_dict,
        validator=attr.validators.optional(attr.validators.instance_of(PlaceIndexDataSourceConfiguration)),
        metadata={AttrMeta.PROPERTY_NAME: "DataSourceConfiguration"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-datasourceconfiguration"""
    p_Description: TypeHint.intrinsic_str = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(TypeCheck.intrinsic_str_type)),
        metadata={AttrMeta.PROPERTY_NAME: "Description"},
    )
    """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#cfn-location-placeindex-description"""

    
    @property
    def rv_CreateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#aws-resource-location-placeindex-return-values"""
        return GetAtt(resource=self, attr_name="CreateTime")
    
    @property
    def rv_IndexArn(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#aws-resource-location-placeindex-return-values"""
        return GetAtt(resource=self, attr_name="IndexArn")
    
    @property
    def rv_UpdateTime(self) -> GetAtt:
        """Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-placeindex.html#aws-resource-location-placeindex-return-values"""
        return GetAtt(resource=self, attr_name="UpdateTime")
    
