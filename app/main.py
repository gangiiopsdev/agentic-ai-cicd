from fastapi import FastAPI
import subprocess
cfrom shlex import quote

capp = FastAPI()

c@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}