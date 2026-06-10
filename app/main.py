from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., allow only certain IP ranges)
    return host in ['example.com', '192.168.0.1']  # Example valid hosts

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(["ping", host], check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr.decode()}

# Ensure that the app object is not redefined elsewhere in your codebase.