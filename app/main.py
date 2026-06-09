from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr if result.returncode != 0 else None
    }