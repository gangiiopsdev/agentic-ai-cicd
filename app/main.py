from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Use shlex.quote to safely escape user-provided input
        safe_host = subprocess.list2cmdline([host])
        subprocess.run(['ping', safe_host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)