from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if host in ['127.0.0.1', '::1']:  # Allow only localhost access for demonstration purposes
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Access denied"}