from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error pinging {host}: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Implement logic to check if the host is safe (e.g., whitelist)
    return host in ["example.com", "another-example.com"]