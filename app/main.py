from fastapi import FastAPI
import subprocess
def ping(host: str):
    sanitized_host = subprocess.quote(host)
    generate_ping_command = subprocess.Popen(['ping', sanitized_host], stdout=subprocess.PIPE)
    output, error = generate_ping_command.communicate()
    if error:
        return {'status': 'error', 'error': error.decode()}
    return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = subprocess.quote(host)
    generate_ping_command = subprocess.Popen(['ping', sanitized_host], stdout=subprocess.PIPE)
    output, error = generate_ping_command.communicate()
    if error:
        return {'status': 'error', 'error': error.decode()}
    return {'status': 'completed', 'output': output.decode()}