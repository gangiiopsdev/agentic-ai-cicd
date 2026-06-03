from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = subprocess.run(generate_ping_command(host), check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}