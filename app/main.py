from fastapi import FastAPI
import subprocess
def execute_command(command):
    return subprocess.run(command, check=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host or len(host) > 100 or any(char in host for char in [';', '&', '|', '>', '<', '*', '?', '~', '`']):
        return {'status': 'error', 'message': 'Invalid input'}
    safe_host = subprocess.list2cmdline([host])
    command = ['ping', safe_host]
    result = execute_command(command)
    return {'status': 'completed', 'output': result.stdout}