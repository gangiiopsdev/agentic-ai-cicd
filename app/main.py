from fastapi import FastAPI
import subprocess
global allowed_hosts = {'example.com'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in allowed_hosts:
        # Use subprocess.run for safer command execution
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}