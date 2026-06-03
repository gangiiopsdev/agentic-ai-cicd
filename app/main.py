from fastapi import FastAPI
import subprocess
def generate_ping_command(host: str):
    # Sanitize or validate the host input
    if not host.isalnum():
        raise ValueError('Invalid host input')
    return f'ping {host}'
app = FastAPI()
@app.get('/ping')
def ping(host: str):    result = subprocess.run(generate_ping_command(host), shell=False, capture_output=True, text=True)    return {'status': 'completed', 'output': result.stdout}