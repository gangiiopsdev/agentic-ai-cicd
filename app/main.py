from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host and len(host.split()) == 1:
        try:
            response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return response.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if host.isalnum():
        return safe_ping(host)
    else:
        return 'Invalid input'