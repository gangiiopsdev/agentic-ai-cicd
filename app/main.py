from fastapi import FastAPI
import subprocess
def validate_host(host):
    return host.isalnum()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid input'}, 400
    command = ['ping', f'-c 1 {host}']  # Limit the number of pings to prevent DoS
    subprocess.run(command, shell=False, check=True)
    return {'status': 'completed'}