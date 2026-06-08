from fastapi import FastAPI
import subprocess
import shlex
global_params = {'host': ''}

app = FastAPI()

def safe_ping(host: str):
    try:
        subprocess.run(['ping', shlex.quote(host)], check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

@app.get('/ping')
def ping(host: str):
    global_params['host'] = host
    return safe_ping(host)