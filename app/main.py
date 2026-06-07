from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return shlex.quote(host)

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        output = subprocess.run(['ping', '-c 1', escaped_host], capture_output=True, text=True, timeout=5)
        if output.returncode == 0:
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'failed', 'error': output.stderr}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': 'Command timed out'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}