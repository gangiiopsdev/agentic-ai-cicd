from fastapi import FastAPI
import subprocess
generate_ping_command = subprocess.Popen(['ping', host], stdout=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output, error = generate_ping_command.communicate()
    if error:
        return {'status': 'error', 'error': error.decode()}
    return {'status': 'completed', 'output': output.decode()}