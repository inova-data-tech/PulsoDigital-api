from fastapi import FastAPI
from app.api.routes import theme, topic, data_source, dashboard, healthcheck

app = FastAPI()

app.include_router(healthcheck.router, prefix="/api", tags=["Healthcheck"])
app.include_router(theme.router, prefix="/api/themes", tags=["Themes"])
app.include_router(topic.router, prefix="/api/topics", tags=["Topics"])
app.include_router(data_source.router, prefix="/api/data-sources", tags=["DataSources"])
app.include_router(dashboard.router, prefix="/api/dashboards", tags=["Dashboards"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
