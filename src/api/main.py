from typing import Union, Any, List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, selectinload

from src.models.models import *

from src.db.sqlite import *

app = FastAPI()


@app.get("/projects/{project}/datasources")  # response_model=List[DataSource]) TODO map to pydantic
async def get_datasources(project: str, db: Session = Depends(get_db)):
    return [db.query(DataSourceDB).options(selectinload(DataSourceDB.attributes)).all()]  # TODO update model to include project name


@app.get("/projects/{project}/datasources/{data_source_id}")
async def get_datasource(project: str, data_source_id: str):
    return "datasources", "message", "detail"


@app.get("/projects")  # response_model=List[Project]) TODO figure out how to map to pydantic
async def get_projects(db: Session = Depends(get_db)):
    return [project.name for project in db.query(ProjectDB).all()]


@app.get("/projects/{project}/features")
async def get_features(project: str, page: Union[int, None] = None, limit: Union[int, None] = None,
                       keyword: Union[str, None] = None):
    return ["features"]


@app.get("/features/{featureId}")
async def get_feature(featureId: str, project: Union[str, None] = None):
    return "feature"


@app.get("features/{featureId}/lineage")
async def get_lineage(featureId: str):
    return "lineage"


# TODO untested code for feature publishing / manipulation
# TODO add endpoints for users, entities and anchors

@app.post("/feature")
async def create_feature(feature: Feature):
    return feature


@app.put("/feature/{featureId}")
async def update_feature(feature: Feature, featureId: Any):
    return "update feature"


# TODO delete misc function
@app.post("/projects", response_model=Project)
async def create_project(project: Project, db: Session = Depends(get_db)):
    project = ProjectDB(name=project.name)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@app.post("/datasource", response_model=DataSource)
async def create_datasource(data_source_input: DataSource, db: Session = Depends(get_db)):
    data_source = DataSourceDB(
        display_text=data_source_input.display_text,
        guid=data_source_input.guid,
        last_modified_ts=data_source_input.last_modified_ts,
        status=data_source_input.status,
        type_name=data_source_input.type_name,
        version=data_source_input.version,
        attributes=DataSourceAttributesDB(**data_source_input.attributes.dict())
    )
    db.add(data_source)
    db.commit()
    db.refresh(data_source)
    return data_source_input
