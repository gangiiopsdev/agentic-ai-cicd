from fastapi import FastAPI
import subprocess
def validate_host(host):
    return all(c.isalnum() or c in '-' for c in host)
def safe_ping(host):
    allowed_hosts = ['example.com', '192.168.1.1']
    if not validate_host(host) or host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', '--', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}