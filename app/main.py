from fastapi import FastAPI
import subprocess
from shlex import quote
def escape_input(input_str):
    return input_str.replace(';', '').replace('&', '')

cmd = ['ping', '-c 1']
cmd.extend(quote(escape_input(host)).split())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.isalnum():
            raise ValueError("Invalid host input")
        # Using subprocess.run instead of subprocess.call for better security
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}