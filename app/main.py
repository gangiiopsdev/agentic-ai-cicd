from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize input
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid host'}
    generate_ping_command = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, shell=False)
    output, error = generate_ping_command.communicate()
    if error:
        return {'status': 'error', 'error': error.decode()}
    return {'status': 'completed', 'output': output.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return ping(host)