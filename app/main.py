from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum():
            return {"error": "Invalid host name"}
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}