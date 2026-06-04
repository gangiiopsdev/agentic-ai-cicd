from fastapi import FastAPI
import subprocess
import re
cimport os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not host.isalnum() and '.' in host:
        raise ValueError('Invalid host format')
    result = subprocess.run(['ping', '-c 1', f'"{host}"'], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}