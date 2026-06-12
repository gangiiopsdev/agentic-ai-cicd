from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_command_input(input_str):
    return input_str.replace(';', '').replace('&', '')

@app.get('/ping')
def ping(host: str):
    # Secure implementation with command input escaping
    escaped_host = escape_command_input(host)
    try:
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}