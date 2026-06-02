from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    ping_command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(ping_command, stdout=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'status' in result and result['status'] == 'error':
        return result
    else:
        return {'status': 'completed'}