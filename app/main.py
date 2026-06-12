from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call for better control and safety
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it only contains allowed characters
    if not host.isalnum():
        return 'Invalid input'
    return safe_ping(host)