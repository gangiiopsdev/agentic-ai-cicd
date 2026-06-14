from fastapi import FastAPI
import os

app = FastAPI()

def safe_ping(host: str):
    # Safer implementation using os.system with validation
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    command = f'ping {host}''
    output = os.popen(command).read()
    return output

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}