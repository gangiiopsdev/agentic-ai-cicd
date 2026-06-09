from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_shell_command(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char in '-_.')

@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell_command(host.strip())
    if not safe_host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}