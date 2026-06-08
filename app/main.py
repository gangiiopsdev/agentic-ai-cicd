from fastapi import FastAPI
import subprocess
def safe_command(cmd):
    return [c for c in cmd.split() if c.isalnum()]

app = FastAPI()

@app.get("/execute")
def execute_command(command: str):