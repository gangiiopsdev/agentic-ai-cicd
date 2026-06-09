from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = ['ping'] + shlex.split(host)
        subprocess.run(args, check=True, shell=False)
        return {'result': 'Success'}
    except subprocess.CalledProcessError as e:
        return {'result': 'Failure', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    return ping(host)