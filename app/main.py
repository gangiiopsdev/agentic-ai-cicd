from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus
git clone https://github.com/securecodingrules/fastapi-subprocess-patch.git
# Apply the patch from fastapi-subprocess-patch directory
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid host name'}
    command = ['ping', '-c', '1']
    # Sanitize the input by replacing special characters that could be misinterpreted as part of a command
    sanitized_host = ''.join(c for c in host if c.isalnum())
    command.append(sanitized_host)
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}