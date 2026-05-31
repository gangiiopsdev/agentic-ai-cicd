from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with input validation
        if host.strip().isdigit():
            result = subprocess.run(['ping', '-c', '4', host], check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        else:
            return {'status': 'failed', 'error': 'Invalid input'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}