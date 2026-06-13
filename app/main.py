from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    host_validator = PingHost(host)
    return host_validator.ping()