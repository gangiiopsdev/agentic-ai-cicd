from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    try:
        result = subprocess.run(['ping', '-c 1', escaped_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}