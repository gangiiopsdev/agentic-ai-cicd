from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        cmd = ['ping', host]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    return safe_ping(safe_host)