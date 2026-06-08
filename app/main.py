from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if not host or '||' in host or ';' in host or '&' in host:
        return "Invalid input"
    return run_ping(host)