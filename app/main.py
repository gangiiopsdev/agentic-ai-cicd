from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        return subprocess.call(['ping', host]) == 0
    else:
        raise ValueError('Unauthorized access')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        if result:
            return {'status': 'completed'}
        else:
            return {'error': 'Ping failed'}, 500
    except ValueError as e:
        return {'error': str(e)}, 403