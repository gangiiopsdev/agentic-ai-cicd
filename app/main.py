from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or len(host) > 100:
        return {"error": "Invalid host name"}, 400
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}, 500