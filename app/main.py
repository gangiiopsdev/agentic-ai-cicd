from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
domain_whitelist = {'google.com', 'facebook.com', 'example.com'}

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    if request.host not in domain_whitelist:
        return {'status': 'failed', 'error': 'Hostname not allowed'}
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional recommendations for improvement:
# 1. Use an allowlist of allowed hosts instead of validation.
# 2. Consider using a more secure method to execute system commands, such as using a library designed for this purpose.