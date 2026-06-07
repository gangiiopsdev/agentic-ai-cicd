from fastapi import FastAPI
import subprocess
import shlex
class PingRequest(BaseModel):
    host: str
app = FastAPI()
allowed_hosts = ['example.com', 'test.com']  # Add your list of allowed hosts here
@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    if not request.host in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping -c 1 {shlex.quote(request.host)}')
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode == 0:
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': ''}
    else:
        return {'status': 'error', 'message': result.stderr}