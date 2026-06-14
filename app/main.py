from fastapi import FastAPI
import re
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9-.]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}