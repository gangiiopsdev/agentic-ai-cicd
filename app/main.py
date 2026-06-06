from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape the host parameter
        subprocess.run(['ping', shlex.quote(host)], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)