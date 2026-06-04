from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safer implementation using subprocess.run with shell=False
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}