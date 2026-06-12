from fastapi import FastAPI
import subprocess

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {"status": "failed", "error": "Host not allowed"}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls
# 1. Use a whitelist of allowed hosts
# 2. Sanitize input using regex or validation libraries