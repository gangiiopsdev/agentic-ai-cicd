from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input by validating and escaping any potentially harmful characters
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}