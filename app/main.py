from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host):
    if not host.isalnum():
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not validate_input(host):
        return {'error': 'Invalid input'}, 400
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500