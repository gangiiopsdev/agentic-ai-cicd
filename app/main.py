from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True, result.stdout.decode(), None
    except subprocess.CalledProcessError as e:
        return False, None, str(e)

@app.get('/ping')
def ping(host: str):
    success, output, error = safe_ping(host)
    if success:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'failed', 'error': error}