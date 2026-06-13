from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(input_str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in input_str):
        return False
    return True

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not validate_input(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', str(1), host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}