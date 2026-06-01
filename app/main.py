from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    return shlex.quote(user_input)

@app.get('/ping/{host}')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        # Use subprocess.run instead of subprocess.call for better control and safety
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}