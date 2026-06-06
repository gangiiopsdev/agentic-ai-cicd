from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize host to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        cmd = ['ping', host]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}