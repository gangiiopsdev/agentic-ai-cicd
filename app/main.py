from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {'status': 'error', 'message': 'Invalid host format'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}