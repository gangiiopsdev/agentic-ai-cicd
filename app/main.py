from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to prevent command injection
    if '||' in host or ';' in host or '&' in host or '`' in host:
        raise ValueError('Invalid characters in host parameter')
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)