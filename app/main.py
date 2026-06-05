from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    cmd = ['ping', host]
    try:
        subprocess.run(cmd, check=True)
        return {"status": "completed", "result": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "result": str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not is_valid_host(host):
        return {"status": "invalid", "result": "Host is invalid"}
    return safe_ping(host)

# Function to validate host input
def is_valid_host(host: str) -> bool:
    # Simple validation, replace with more robust checks as needed
    return all(c.isalnum() or c in ['.', '-'] for c in host)