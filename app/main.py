from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(cmd_parts):
    cmd = [shlex.quote(part) for part in cmd_parts]
    return ' '.join(cmd)

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    safe_cmd = safe_command(['ping', host])
    subprocess.run(safe_cmd, shell=True)
    return {'status': 'completed'}