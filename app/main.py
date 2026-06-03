from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use shlex.quote to safely quote the host parameter
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}