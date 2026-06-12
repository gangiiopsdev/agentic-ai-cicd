from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return input_str.strip().replace(';', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}