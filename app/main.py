from fastapi import FastAPI
import subprocess
global ping_command_template
ping_command_template = ['ping', '{host}']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
            raise ValueError("Invalid hostname")
        subprocess.run(ping_command_template + [host], check=True)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}