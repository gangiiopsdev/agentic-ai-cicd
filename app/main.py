from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        return {"error": "Invalid input"}
    response = safe_ping(host)
    return {"status": "completed", "response": response}