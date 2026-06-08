from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        host_parts = shlex.split(host)
        if any(char in host_parts for char in [';', '&', '|', '>', '<', '\\']):  # Basic validation to prevent injection
            return {'status': 'failed', 'error': 'Invalid input'}
        output = subprocess.check_output(['ping'] + host_parts, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)