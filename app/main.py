from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def execute_safe_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping(host):
    command = ["ping", quote(host)]
    output = execute_safe_command(command)
    return output

@app.get("/ping")
def ping(host: str):
    return {"status": "completed", "output": safe_ping(host)}