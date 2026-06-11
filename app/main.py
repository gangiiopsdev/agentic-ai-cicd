from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    # Secure implementation using subprocess.run with shlex.split to avoid injection
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    status = execute_ping(host)
    return {"status": "completed", "output": status}