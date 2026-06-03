from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only specific domains
    return host.strip() in ['localhost', '127.0.0.1']

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'Invalid host'}, 400

    # Secure implementation
    subprocess.run(['ping', host], check=True)

    return {'status': 'completed'}