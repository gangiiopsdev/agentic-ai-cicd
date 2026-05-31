from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(generate_ping_command(host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': subprocess.run(generate_ping_command(host), check=True, capture_output=True, text=True).stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}