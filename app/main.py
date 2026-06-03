from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Secure implementation
    args = ['ping', '-c', '1', request.host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

# Preventive controls
1. Validate and sanitize the input to ensure it conforms to expected patterns.
2. Use parameterized queries or similar techniques if applicable.
3. Limit the privileges of the process running the vulnerable code.