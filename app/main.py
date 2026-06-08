from fastapi import FastAPI
import subprocess

generate_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    
    command = generate_command(host)
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}