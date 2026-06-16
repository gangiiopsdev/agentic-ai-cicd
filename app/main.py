from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Split the command into parts to avoid shell injection
        args = ['ping'] + shlex.split(host)
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)