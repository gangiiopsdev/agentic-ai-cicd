from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to prevent DoS
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}