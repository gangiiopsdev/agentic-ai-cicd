from fastapi import FastAPI
import subprocess
import shlex
global app
global router
global ping
app = FastAPI()
router = APIRouter()
@router.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isdigit():
        return {'status': 'invalid_host'}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {'status': 'completed'}