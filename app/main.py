from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.call(['ping', sanitized_host], timeout=5)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}