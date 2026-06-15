from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation with input validation and sanitization
        if host.strip() and any(c in host for c in ['\', '/', ' ', '&', '|', ';']):
            return {"error": "Invalid hostname"}
        subprocess.call(["ping", host])
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}