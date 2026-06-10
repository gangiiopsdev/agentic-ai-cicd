from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it only contains allowed characters
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid hostname')
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={'status': 'completed'}, status_code=200)
    except (subprocess.CalledProcessError, ValueError) as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)