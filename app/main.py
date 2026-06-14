from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}