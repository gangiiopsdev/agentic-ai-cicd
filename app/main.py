from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {"error": "Host is required and cannot be empty."}
    args = ["ping", host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }