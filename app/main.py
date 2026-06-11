from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input by escaping special characters or using a whitelist approach
    sanitized_host = host.replace(';', '').replace('&', '')  # Example sanitization, adjust as needed
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}