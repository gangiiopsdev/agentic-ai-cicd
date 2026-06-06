from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Use a safe method without shell=True and validate input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    try:
        # Call the safe function and handle exceptions
        result = ping_safe(host)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}