from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e == '.')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host = sanitize_input(host)
    # Validate the host input
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", host])
    return {"status": "completed"}