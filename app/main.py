from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not validate_host(host):
        return {'status': 'invalid host'}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}

# Function to validate host input
def validate_host(host: str) -> bool:
    # Add your validation logic here (e.g., allow only specific domains or IP addresses)
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts