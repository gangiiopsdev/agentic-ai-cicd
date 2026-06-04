from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Basic validation of host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host) or len(host) > 255:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}