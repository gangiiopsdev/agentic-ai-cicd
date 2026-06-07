from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        result = await asyncio.create_subprocess_exec('ping', self.host)
        return await result.wait()

class PingEndpoint:
    @staticmethod
    def ping(host: str):
        try:
            # Validate the host input using a whitelist or regex
            if not re.match(r'^[a-zA-Z0-9.-]+$', host):
                raise ValueError('Invalid host format')
        except ValueError as e:
            return {'error': str(e)}, 400

        pinger = PingHost(host)
        return {'status': 'completed'}, await pinger.ping()

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingEndpoint.ping(host)