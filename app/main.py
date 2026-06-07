from fastapi import FastAPI
import asyncio

async def safe_ping(host: str):
    # Safe implementation using subprocess.run with proper arguments and validation
    allowed_hosts = ['google.com', 'example.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return 'Invalid host'
    args = ['ping', '-c', '1', host]  # Use -c to limit the number of pings to avoid resource exhaustion
    result = await asyncio.subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_api_route('/', self.home)
        self.app.add_api_route('/ping', self.ping)

    async def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}

    async def ping(self, host: str):
        output = await safe_ping(host)
        return {'status': 'completed', 'output': output}

app_instance = FastAPIApp().app