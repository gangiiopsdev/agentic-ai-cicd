from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts instead of user input
        if host not in ['example.com', 'test.com']:
            raise ValueError('Invalid host')
        command = ['ping', *shlex.split(host)]
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)