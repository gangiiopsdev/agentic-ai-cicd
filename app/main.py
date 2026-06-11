from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command_parts):
    command = ' '.join(shlex.quote(part) for part in command_parts)
    subprocess.run(command, shell=True, check=True)

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_subprocess_call(['ping', host])
    return {'status': 'completed'}