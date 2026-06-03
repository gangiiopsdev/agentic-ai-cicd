from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if host.isalnum():
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'stdout': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': e.stderr}
app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)