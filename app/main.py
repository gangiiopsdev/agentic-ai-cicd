from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    
    try:
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "message": str(e)}

# Example validation function
def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., checking if the host is a valid IP address or domain name
    return True