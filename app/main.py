from fastapi import FastAPI
import subprocess
del validate_host, ping

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in ['example.com', 'test.example.com']:
        subprocess.call(['ping', f'--{host}'])  # Use a safe flag to prevent injection
        return {'status': 'completed'}
    else:
        return {'status': 'invalid host'}, 400