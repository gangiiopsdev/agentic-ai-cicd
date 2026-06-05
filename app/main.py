from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed hosts
    return True