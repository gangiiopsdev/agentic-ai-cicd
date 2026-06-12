from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ["ping", host]
    result = subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}