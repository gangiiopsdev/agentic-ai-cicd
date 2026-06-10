from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead and avoid shell=True for security reasons.
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Untrusted host')
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Implement logic to check if the host is safe
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts