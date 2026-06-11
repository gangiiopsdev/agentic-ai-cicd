from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    allowed_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        return {"error": "Invalid host"}
    try:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}