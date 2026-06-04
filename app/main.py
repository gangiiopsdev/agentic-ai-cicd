from fastapi import FastAPI
import subprocess
import shlex
def shell_quote(s):
    return shlex.quote(s)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', shell_quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}