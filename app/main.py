from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid input")
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}