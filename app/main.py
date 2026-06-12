from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 400

    # Secure implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}