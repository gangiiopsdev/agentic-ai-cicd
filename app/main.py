from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with a full path for 'ping'
    subprocess.run(['/bin/ping', shlex.quote(host)], check=True, capture_output=True)
    return {'status': 'completed'}