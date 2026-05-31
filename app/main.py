from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.strip().isdigit():
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', '-c', '4', f'/bin/ping'], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}