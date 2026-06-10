from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    if not input_string or len(input_string) > 255:
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', f'"{host}"'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}