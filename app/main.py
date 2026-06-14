from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls
# 1. Validate and sanitize input to ensure it does not contain malicious commands.
# 2. Use parameterized queries if applicable.
# 3. Consider using a whitelist of allowed hosts or IPs.