from fastapi import FastAPI
import subprocess
def get_command(host: str) -> list:
    return ['ping', '-c', '1', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Validate input to prevent injection
        return {'error': 'Invalid input'}
    try:
        result = subprocess.run(get_command(host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}