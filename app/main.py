from fastapi import FastAPI
import re
import subprocess
class PingService:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'test.com'}

    async def is_safe_input(self, input_str):
        return re.match(r'^[a-zA-Z0-9.-]+$', input_str) and input_str in self.allowed_hosts

app = FastAPI()
ping_service = PingService()

@app.post('/ping/')
def ping(host: str):
    if not ping_service.is_safe_input(host):
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}