from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True)
    return {'status': 'completed'}