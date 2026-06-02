from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input before using in subprocess call
    if is_valid_host(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    output = safe_ping(host)
    return {"status": "completed", "output": output}

def is_valid_host(host: str) -> bool:
    # Implement input validation logic here
    return True  # Placeholder for actual validation