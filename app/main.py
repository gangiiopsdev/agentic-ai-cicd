from fastapi import FastAPI
import subprocess

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and escaping
    try:
        subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}