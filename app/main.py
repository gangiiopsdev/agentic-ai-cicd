from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.output}
    return {"status": "completed", "output": output}