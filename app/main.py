from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Simple example of sanitization, replace with appropriate logic
    return ''.join(e for e in input_str if e.isalnum() or e.isspace())

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', '-c 1', sanitized_host], check=True, text=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}