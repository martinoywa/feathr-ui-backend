from typing import List, Dict, Any
from pydantic import BaseModel


class Project(BaseModel):
    name: str


class FeatureTransformation(BaseModel):
    transformExpr: str = None
    filter: str = None
    aggFunc: str = None
    limit: str = None
    groupBy: str = None
    window: str = None
    defExpr: str = None
    udfExpr: str = None


class FeatureKey(BaseModel):
    description: str
    fullName: str
    keyColumn: str
    keyColumnAlias: str
    keyColumnType: str


class InputFeatureAttributes(BaseModel):
    qualifiedName: str
    version: str


class InputFeature(BaseModel):
    guid: str
    typeName: str
    uniqueAttributes: InputFeatureAttributes


class FeatureType(BaseModel):
    dimensionType: List[str]
    tensorCategory: str
    type: str
    valType: str


class FeatureAttributes(BaseModel):
    inputAnchorFeatures: List[InputFeature]
    inputDerivedFeatures: List[InputFeature]
    key: List[FeatureKey]
    name: str
    qualifiedName: str
    tags: Dict[str, Any]
    transformation: FeatureTransformation
    type: FeatureType


class Feature(BaseModel):
    attributes: FeatureAttributes
    displayText: str
    guid: str
    labels: List[str]
    name: str
    qualifiedName: str
    status: str
    typeName: str
    version: str


class DataSourceAttributes(BaseModel):
    eventTimestampColumn: str
    name: str
    path: str
    preprocessing: str
    qualifiedName: str
    tags: List[str]
    timestampFormat: str
    type: str


class DataSource(BaseModel):
    attributes: DataSourceAttributes
    displayText: str
    guid: str
    lastModifiedTS: str
    status: str
    typeName: str
    version: str


class RelationData(BaseModel):
    fromEntityId: str
    relationshipId: str
    relationshipType: str
    toEntityId: str


class FeatureLineage(BaseModel):
    guidEntityMap: Dict[str, Feature]
    relations: List[RelationData]


class UserRole(BaseModel):
    id: int
    scope: str
    userName: str
    roleName: str
    createBy: str
    createTime: str
    createReason: str
    deleteBy: str
    deleteTime: Any = None
    deleteReason: Any = None
    access: str = None


class Role(BaseModel):
    scope: str
    userName: str
    roleName: str
    reason: str


class NewFeature(BaseModel):
    name: str
    featureType: FeatureType
    transformation: FeatureTransformation
    key: List[FeatureKey] = None
    tags: Dict[str, Any] = None
    inputAnchorFeatures: List[str] = None
    inputDerivedFeatures: List[str] = None
    # qualifiedName: str = None


class NewDatasource(BaseModel):
    eventTimestampColumn: str = None
    name: str
    path: str = None
    preprocessing: str = None
    qualifiedName: str
    tags: Dict[str, Any]
    timestampFormat: str = None
    type: str

    sourceType: str = None
    url: str = None
    dbtable: str = None
    query: str = None
    auth: str = None

    format: str = None
    spark_cosmos_accountKey: str = None
    spark_cosmos_accountEndpoint: str = None
    spark_cosmos_database: str = None
    spark_cosmos_container: str = None

    endpoint: str = None
    container: str = None

    sql: str = None
    table: str = None
