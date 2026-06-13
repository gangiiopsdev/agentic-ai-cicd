from fastapi import FastAPI
import subprocess
global args
args = {"ping": {"description": "Pings a specified host. Usage: /ping?host=example.com", "parameters": [{"name": "host", "in": "query", "required": true, "schema": {"type": "string"}}]}}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/docs")
def docs():
    return args