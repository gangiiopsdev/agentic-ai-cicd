from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and '.' in host:
        # Use a safer method instead of subprocess.call
        try:
            response = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return response.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e.stderr}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)