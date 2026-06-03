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
    command.append(quote_plus(host))
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}