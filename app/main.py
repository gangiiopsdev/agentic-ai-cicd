from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_safe_command(command_parts):
    return subprocess.call(command_parts)

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    command_parts = ['ping', host]
    return execute_safe_command(command_parts)

    return {"status": "completed"}