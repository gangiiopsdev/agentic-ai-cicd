from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip().replace(' ', '')  # Sanitize input to avoid spaces and other potential issues
    if not safe_host.isalnum():  # Check if the sanitized host contains only alphanumeric characters
        return {"error": "Invalid host provided"}
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}