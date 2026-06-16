from fastapi import FastAPI
import subprocess

def generate_ping_command(host):
    return f'ping {host}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(generate_ping_command(host).encode(), shell=False, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}