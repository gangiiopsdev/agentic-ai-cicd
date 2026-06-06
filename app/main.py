from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        result = await asyncio.create_subprocess_exec('ping', self.host)
        return await result.wait()  # Wait for the process to finish and get its exit code

class PingEndpoint:
    @staticmethod
def ping(host: str):
        try:
            host = validate_host(host)  # Assume this function validates the host input
        except ValueError as e:
            return {'error': str(e)}, 400

        pinger = PingHost(host)
        return {'status': 'completed'}, await pinger.ping()

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingEndpoint.ping(host)