from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    status = safe_ping(host)
    return {"status": "completed", "output": status}

def valid_host(host):
    import re
    pattern = r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{1,61}[a-zA-Z0-9])$'
    return re.match(pattern, host) is not None