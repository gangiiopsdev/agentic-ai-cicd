from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        if safe_ping(host):
            result = subprocess.run(['/bin/ping', '--', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'error', 'message': 'Host not allowed'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}