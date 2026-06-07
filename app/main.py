from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        cmd = ['ping'] + [shlex.quote(h) for h in host.split()]
        subprocess.run(cmd, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)