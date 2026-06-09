from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        host = shlex.quote(host)
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}