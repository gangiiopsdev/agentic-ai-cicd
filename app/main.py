from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using shlex.quote to escape arguments
    args = ['ping', shlex.quote(host)]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(shlex.quote(host))