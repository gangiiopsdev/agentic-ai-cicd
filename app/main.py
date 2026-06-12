from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        return True, host
    return False, None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '4', f'"{host}"'], capture_output=True, text=True, check=True)
            return {'status': 'success', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}
    else:
        return {'status': 'error', 'output': 'Host not allowed'}