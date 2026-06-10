from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run instead of subprocess.call
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, str):
        return {"status": "failed", "error": result}
    else:
        return {"status": "completed"}