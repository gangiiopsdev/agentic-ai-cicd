from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' in host or '&' in host:
        raise ValueError('Unsafe input detected')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'error', 'message': str(e)}