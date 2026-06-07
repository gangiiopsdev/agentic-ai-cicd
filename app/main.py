from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to avoid injection attacks
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split('ping {}'.format(host)), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}