from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if not host.strip().replace('.', '', 1).isdigit():
        return False
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if output.returncode != 0:
            return {'status': 'failed', 'error': output.stderr}
        else:
            return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result['status'] == 'failed':
        return result
    else:
        return result