from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
global hosts
hosts = ['127.0.0.1']
security_scheme = HTTPBearer()
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str, credentials: HTTPAuthorizationCredentials = Depends(security_scheme)):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 403
    try:
        result = subprocess.run(['ping', f'--{host}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500
    except Exception as e:
        return {'error': str(e)}, 500
def is_valid_host(host):
    # Add your validation logic here, e.g., check if the host is in a whitelist.
    return host in hosts