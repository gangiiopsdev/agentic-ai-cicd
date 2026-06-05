from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    # Add your validation logic here
    return host.startswith('192.168.')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}