from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe to use with ping
    if not host.strip().replace('.', '').isnumeric():
        return 'Invalid host'
    return safe_ping(host)