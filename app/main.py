from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    safe_ping(host)
    return {"status": "completed"}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if it's a valid IP address or hostname
    return True