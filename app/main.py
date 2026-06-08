from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', '-c', '4', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': command[2]}  # Output the host name
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}