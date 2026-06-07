from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(value: str) -> str:
    if not (value.isalnum() or '.' in value):
        raise ValueError('Invalid hostname')
    return shlex.quote(value)

@app.get('/ping')
def ping(host: str):
    safe_command = ['ping', sanitize_input(host)]
    try:
        subprocess.run(safe_command, check=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}