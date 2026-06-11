from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Unsafe host specified')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return {'status': safe_ping(host)}
    except Exception as e:
        return {'error': str(e)}