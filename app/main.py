from fastapi import FastAPI
import subprocess
def escape_command(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

class PingService:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'test.com'}

    async def is_safe_input(self, input_str):
        return input_str in self.allowed_hosts

app = FastAPI()
ping_service = PingService()

@app.post('/ping/')
def ping(host: str):\n    if not ping_service.is_safe_input(host):
        return {'status': 'error', 'message': 'Invalid input'}\n    args = ['ping', escape_command(host)]\n    result = subprocess.run(args, capture_output=True, text=True, check=True)\n    return {'status': 'completed', 'output': result.stdout}