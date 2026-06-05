from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Basic validation to prevent simple injection attacks
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host) or '/' in host:
        return {
            "status": "failed",
            "error": "Invalid hostname provided"
        }
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": output.stdout
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": e.stderr
        }