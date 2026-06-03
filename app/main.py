from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Use a safer method to avoid shell injection risks
    generate_ping_command = subprocess.run(['ping', host], capture_output=True, text=True)
    if generate_ping_command.stderr:
        return {'status': 'error', 'error': generate_ping_command.stderr}
    return {'status': 'completed', 'output': generate_ping_command.stdout}

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return ping(host)