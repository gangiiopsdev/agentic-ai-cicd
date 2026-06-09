from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command_parts):
    full_command = [part for part in command_parts]
    try:
        subprocess.run(full_command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'status': 'failed'}

@app.get('/ping')
def ping(host: str):
    command_parts = ['ping', host]
    for part in command_parts:
        if not part.isalnum():
            raise ValueError('Invalid input detected in command parts')
    return run_command(command_parts)