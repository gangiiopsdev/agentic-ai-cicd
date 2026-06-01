from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping/{host}')
def ping_host(host: str):
    # Sanitize the host input to prevent injection attacks
    sanitized_host = ''.join(filter(str.isdigit, host))  # Example of basic sanitization
    return ping(sanitized_host)