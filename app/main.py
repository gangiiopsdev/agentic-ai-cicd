from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host input')

    app = FastAPI()

    @app.get('/ping')
    def ping(host: str):
        safe_ping(host)
        subprocess.call(['ping', host])
        return {'status': 'completed'}