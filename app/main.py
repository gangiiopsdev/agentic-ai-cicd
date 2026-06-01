from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with argument validation and sanitization
    if all(c.isalnum() or c in '-.' for c in host):
        subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}