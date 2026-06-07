from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add validation logic here (e.g., regex check)
    return host.strip().endswith('.com')

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    try:
        # Safe implementation using subprocess.run with args and shell=False
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}