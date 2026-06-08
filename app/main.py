from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    return subprocess.run(command, check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = ["ping", host]
    result = execute_command(command)
    return {"stdout": result.stdout.decode(), "stderr": result.stderr.decode() if result.stderr else None}