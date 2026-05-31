from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping -c 1 {host}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(generate_ping_command(host), shell=True, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}