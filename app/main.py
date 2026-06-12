from fastapi import FastAPI
import subprocess
class Config:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

def ping(host: str):
    if host not in Config.ALLOWED_HOSTS:
        return {'error': 'Invalid host'}
    try:
        # Use a safer way to construct the command
        args = ['ping', '-c 1', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}