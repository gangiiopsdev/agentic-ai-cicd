from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific IP addresses or domain names
    return True