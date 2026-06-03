from fastapi import FastAPI
import subprocess
def allowed_hosts(host):
    return host in ['127.0.0.1', '::1']
cmd = lambda h: f'ping {h}' if allowed_hosts(h) else 'echo Invalid input'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not allowed_hosts(host):
        return {'error': 'Invalid input'}
    try:
        output = subprocess.run(cmd(host).split(), capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    else:
        return {'status': 'completed', 'response': output.stdout}