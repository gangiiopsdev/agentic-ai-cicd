from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

@app.get("/ping")
def ping(host: str):

    if not safe_ping(host):
        raise HTTPException(status_code=400, detail="Invalid IP address")

    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}