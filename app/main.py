from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate host input before using it in the command
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to escape special characters
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)
    return {"status": "completed"}

# Function to validate host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed characters and format
    return all(c.isalnum() or c in ['.', '-'] for c in host)