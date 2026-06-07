from fastapi import FastAPI
import subprocess

def generate_ping_command(host):
    return ['ping', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(generate_ping_command(host), check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}