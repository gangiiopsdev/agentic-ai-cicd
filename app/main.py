from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize host input using a whitelist approach
        allowed_hosts = ['google.com', 'example.com']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Host is not allowed'}
        output = subprocess.check_output(['ping', host], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)