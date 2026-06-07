from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation: allow only alphanumeric and some special characters
    return all(c.isalnum() or c in ['.', '-', '_'] for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}