from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return host.strip()

def ping_safe(host):
    if not host:
        raise ValueError("Invalid host")
    try:
        result = subprocess.run(['ping', '-c 1', f'--{host}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return ping_safe(host)