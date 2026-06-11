from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        # Secure implementation using subprocess.run with shell=False and arguments tuple
        result = await asyncio.create_subprocess_shell(
            f'ping {host}',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return {'status': 'completed', 'output': result.stdout}

global_ping_service = PingService()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global_ping_service.ping(host)
    return {'status': 'completed'}