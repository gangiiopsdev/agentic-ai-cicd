from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call for better security
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input before passing it to the function
    if not is_valid_host(host):
        return HTTPException(status_code=400, detail="Invalid host")
    safe_ping(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., check if the host is within a whitelist of allowed hosts)
    return True