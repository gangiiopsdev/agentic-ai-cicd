from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping', '-c 4', host], check=True, capture_output=True)
        return {
            "status": "completed",
            "output": result.stdout.decode('utf-8')
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr.decode('utf-8')
        }

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)