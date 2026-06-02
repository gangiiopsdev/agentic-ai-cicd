from fastapi import FastAPI
import subprocess

generate_random_payload = 'ping 127.0.0.1' # Replace with a safe payload or method

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:
        return {'status': 'error', 'message': 'Invalid host'}

    # Sanitize user input before constructing the command
    sanitized_host = subprocess.list2cmdline([host])
    cmd = [generate_random_payload, '--'] + [sanitized_host]
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}