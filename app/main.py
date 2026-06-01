from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum():
        raise ValueError("Invalid input")
    return host
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    valid_host = validate_host(host)
    args = ['ping', f'-c 1 {valid_host}']
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr)
    return {"status": "completed", "output": result.stdout}