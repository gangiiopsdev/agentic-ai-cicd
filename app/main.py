from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():  # Add validation for alphanumeric characters only
        return "Invalid input"
    try:
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def validate_host(host: str):
    if not host.isalnum():  # Add validation for alphanumeric characters only
        raise ValueError("Invalid input")

@app.get("/ping")
def ping(host: str = Depends(validate_host)):
    return safe_ping(host)