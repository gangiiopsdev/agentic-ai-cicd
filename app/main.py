from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    try:
        if not validate_host(host):
            return {"error": "Invalid host"}, 400
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500

def validate_host(host: str) -> bool:
    # Simple regex to allow only alphanumeric characters and hyphens
    import re
    pattern = r'^[a-zA-Z0-9-]+$'
    return re.match(pattern, host) is not None