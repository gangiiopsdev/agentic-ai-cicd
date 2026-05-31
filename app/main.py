from fastapi import FastAPI
import subprocess
import shlex

global_host = '127.0.0.1'  # Use a safe default or validate host input

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.startswith('192.168.') and not host.startswith('10.'):  # Allow only local networks for example
        raise ValueError('Invalid host')
    full_command = get_full_command(['ping', global_host])
    result = subprocess.run(full_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}