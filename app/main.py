from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split('ping ' + host), capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(shlex.quote(host))