from fastapi import FastAPI
import subprocess
def validate_host(host):
    return all(c.isalnum() or c in '-' for c in host)
def safe_ping(host):
    allowed_hosts = ['example.com', '192.168.1.1']
    if not validate_host(host) or host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', '--', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': output.decode('utf-8'), 'error': error.decode('utf-8') if error else None}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}