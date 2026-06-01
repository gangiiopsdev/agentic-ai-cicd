from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    if any(char in input_string for char in [';', '&', '|', '$', '`']):
        raise ValueError("Invalid characters detected")

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        subprocess.run(['ping', sanitized_host], check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}