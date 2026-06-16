from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    valid_hosts = ['192.168.', '10.0.']
    for valid_host in valid_hosts:
        if host.startswith(valid_host):
            command = ['ping', host]
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
    return {'error': 'Invalid host'}