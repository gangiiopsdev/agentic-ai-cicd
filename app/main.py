from fastapi import FastAPI
import subprocess
global_config = {
    'ping': ['ping']
}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in global_config['ping']:
        return {'status': 'failed', 'error': 'Invalid command'}
    try:
        result = subprocess.run(global_config[host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}