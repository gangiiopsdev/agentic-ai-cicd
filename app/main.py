from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use shlex.quote to safely escape the host parameter
    args = ['ping', '-c', '1'] + shlex.split(host)
    try:
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)