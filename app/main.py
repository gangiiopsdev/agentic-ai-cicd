from fastapi import FastAPI
import subprocess
import shlex
def execute_command(command_parts):
    return subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command_parts = ["ping", host]  # Avoid using shlex.quote
    result = execute_command(command_parts)
    return {"status": "completed", "output": result.stdout.decode()}