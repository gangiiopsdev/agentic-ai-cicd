from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    allowed_hosts = ['google.com', 'example.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Unauthorized host'}, 403
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}