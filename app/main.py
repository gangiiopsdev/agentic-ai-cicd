from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', subprocess.list2cmdline([host])], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    return safe_ping(host)