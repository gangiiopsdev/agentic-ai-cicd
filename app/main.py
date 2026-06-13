from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input more thoroughly
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    command = ["ping", host]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}