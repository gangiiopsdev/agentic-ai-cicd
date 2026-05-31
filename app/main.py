from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    if isinstance(response, dict) and 'status' in response and response['status'] == 'error':
        return response
    else:
        return {'status': 'completed', 'output': response}