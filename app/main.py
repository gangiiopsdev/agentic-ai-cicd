from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(command_parts):
    return ' '.join(shlex.quote(part) for part in command_parts)

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid input'}, 400
    subprocess.call(safe_command(['ping', '-c', '1', host]).split())
    return {'status': 'completed'}