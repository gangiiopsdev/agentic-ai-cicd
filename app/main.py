from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    # Validate host input before using it in the command
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    await safe_ping(host)

    return {"status": "completed"}

# Function to validate host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed characters and format
    return all(c.isalnum() or c in ['.', '-'] for c in host)