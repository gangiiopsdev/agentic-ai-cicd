from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command_parts):
    return subprocess.call(command_parts)

@app.get="/ping")
def ping(host: str):
    command_parts = ["ping", host]
    result = execute_command(command_parts)
    return {"status": "completed"}