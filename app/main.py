from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host and isinstance(host, str) and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return ['ping', host]
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        command = safe_ping(host)
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e)}