from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def escape_user_input(user_input):
    return ''.join(c if c.isalnum() or c in ('.', '-', '_') else '_' for c in user_input)
app = FastAPI()
class PingRequest(BaseModel):
    host: str@app.post('/ping', response_model=PingResponse)
def ping(request: PingRequest):
    escaped_host = escape_user_input(request.host)
    if not escaped_host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', str(1), escaped_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}