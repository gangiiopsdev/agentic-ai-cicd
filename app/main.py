from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.split to safely handle user input
        cmd = shlex.split('ping ' + host)
        subprocess.run(cmd, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)