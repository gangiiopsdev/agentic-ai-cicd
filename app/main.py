from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation to ensure the host does not contain unexpected characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(char in allowed_chars for char in host):
        return True
    return False

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return safe_ping(host)
    else:
        return {"error": "Invalid host"}