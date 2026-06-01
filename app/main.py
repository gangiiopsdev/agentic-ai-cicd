from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid host name'}
    command = ['ping', '-c', '1']
    # Sanitize the host input to avoid shell injection
    sanitized_host = subprocess.list2cmdline([host])
    command.append(sanitized_host)
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}