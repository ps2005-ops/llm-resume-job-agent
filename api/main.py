from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent import run_agent

app = FastAPI(title="Resume Job Agent")

class Query(BaseModel):
    task: str

@app.post("/run")
def run(q: Query):
    return {"result": run_agent(q.task)}
