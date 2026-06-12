from fastapi import FastAPI
import subprocess
def is_safe_hostname(hostname):
    # Implement safe hostname checking logic here
    return all(c.isalnum() or c in ['-', '_'] for c in hostname)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_hostname(host):
        subprocess.run(['ping', host], check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}