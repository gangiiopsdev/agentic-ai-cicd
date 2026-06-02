from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: str):
    args = shlex.split(command)
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = execute_command(command)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }