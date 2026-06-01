from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping -c 1 {host}' if subprocess.__name__ == 'subprocess' else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if generate_ping_command is not None:
        try:
            subprocess.run(generate_ping_command(host), check=True, shell=False)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host parameter'}