from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = ['ping', *shlex.split(host)]
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}
    return {'status': 'completed'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)