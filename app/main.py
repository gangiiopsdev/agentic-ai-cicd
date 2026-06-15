from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Simple escaping for demonstration purposes. Proper implementation may require more sophisticated techniques.
    return host.replace(';', '').replace('&', '')

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}