from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command_parts = ['ping', host]
    try:
        output = subprocess.run(command_parts, check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}