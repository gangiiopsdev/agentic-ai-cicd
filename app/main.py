from fastapi import FastAPI
import subprocess
def escape_command(command):
    return [arg.replace(';', '').replace('&', '') for arg in command]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_command(['ping', host])
    try:
        result = subprocess.run(escaped_host, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}