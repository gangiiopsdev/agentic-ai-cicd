from fastapi import FastAPI
import subprocess
timeout = 5

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and a list of arguments
    if host.strip() not in ['localhost', '127.0.0.1']:  # Restrict hosts to known safe ones
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', str(timeout), host], capture_output=True, text=True, timeout=timeout)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e}'}, 500
    except TimeoutExpired as e:
        return {'status': 'error', 'message': f'Timeout occurred: {e}'}, 504