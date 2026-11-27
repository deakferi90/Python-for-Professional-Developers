from fastapi import FastAPI

app = FastAPI(title="Computer API")


@app.get("/projects")
def list_projects() -> list[dict]:
    return [{"id": 1, "name": "Project 1"}, {"id": 2, "name": "Project 2"}]
