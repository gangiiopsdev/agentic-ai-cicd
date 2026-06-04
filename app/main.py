from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters
    if any(char in host for char in [';', '&', '|', '`', '(', ')']):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}