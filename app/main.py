from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isdigit():
        return {"status": "error", "message": "Invalid input for ping command."}
    # Secure implementation using subprocess.run with shell=False and explicit argument passing
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}