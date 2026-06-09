from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host,
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
            return await result.communicate()
        except Exception as e:
            return str(e)

class PingRouter:
    def __init__(self):
        pass

    async def ping(self, host: str):
        ping_command = PingCommand(host)
        result = await ping_command.execute()
        return {'status': 'completed', 'result': result}

app = FastAPI()
ping_router = PingRouter()

@app.get('/ping')
def ping_route(host: str):
    return ping_router.ping(host)