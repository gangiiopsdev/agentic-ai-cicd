from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum():
        return {"error": "Invalid input"}
    command = ["ping", host]
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}