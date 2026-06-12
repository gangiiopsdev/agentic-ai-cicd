from fastapi import FastAPI
import subprocess
def execute_safe_ping(host: str):
    safe_args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(safe_args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return execute_safe_ping(host)