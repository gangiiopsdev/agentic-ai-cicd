from fastapi import FastAPI
import subprocess
import shlex
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    args = ['ping'] + shlex.split(command)  # Use shlex to safely split the command
    try:
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}