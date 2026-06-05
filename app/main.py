from fastapi import FastAPI
import subprocess
import shlex
import os
def validate_host(host: str) -> bool:
    if not host.strip() or not host.replace('.', '').isnumeric():
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Host parameter is empty, invalid, or contains non-numeric characters"}
    args = ['ping', *shlex.split(f'{host}')] if os.name == 'posix' else ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}