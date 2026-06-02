from fastapi import FastAPI
import httpx

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://{httpx.URL(host).host}')
            return response.text

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it with subprocess
    if not host or not httpx.URL(host).is_valid:
        return {'status': 'error', 'result': 'Invalid host'}
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}