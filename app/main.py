from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or host.strip() == '':
        raise ValueError('Invalid host')
    command = ["ping", f'\\{host}']  # Escape the backslash to prevent shell injection
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}