from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host:
        return {'status': 'failed', 'message': 'Invalid input'}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'message': str(e)}