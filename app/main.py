from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', '-c', '1', subprocess.check_output(host.encode(), shell=False, stderr=subprocess.STDOUT).decode()]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed', 'output': result.stdout}