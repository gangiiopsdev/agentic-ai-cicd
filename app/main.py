from fastapi import FastAPI
import subprocess
import shlex

global safe_hosts
safe_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in safe_hosts:
        return {'status': 'error', 'message': 'Unauthorized host'}
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}