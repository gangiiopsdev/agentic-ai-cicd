from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def sanitize_input(self, input_str):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
        return ''.join(char for char in input_str if char in allowed_chars)

    async def ping(self, host: str):
        sanitized_host = self.sanitize_input(host)
        args = shlex.split(f'ping {sanitized_host}')
        await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)