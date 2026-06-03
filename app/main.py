from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host: str):
    try:
        cmd = ['ping', host]
        output = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)