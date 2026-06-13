from fastapi import FastAPI
import subprocess
globally_configured_hosts = ['127.0.0.1'] # Configure a whitelist of allowed hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_configured_hosts:
        safe_host = subprocess.quote(host)
        command = ['ping', safe_host]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        raise ValueError('Invalid host')