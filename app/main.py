from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def get_full_command(command_parts):
    return command_parts

def safe_ping(host):
    if not host.startswith('192.168.') and not host.startswith('10.'):  # Allow only local networks for example
        raise ValueError('Invalid host')
    full_command = ['ping', shlex.quote(host)]
    try:
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)