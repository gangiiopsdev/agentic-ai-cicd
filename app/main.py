from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # More robust validation of input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid input"
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def validate_host(host: str):
    # Additional validation logic can be added here
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str):  # Removed type hint for simplicity
    try:
        validate_host(host)
        result = safe_ping(host)
        return {"message": result}
    except ValueError as e:
        return {"error": str(e)}