from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    if not host.startswith('192.168.'):
        return {'status': 'invalid_host'}
    ping_command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)