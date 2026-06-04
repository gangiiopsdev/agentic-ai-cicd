from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    async def ping(self, host: str):
        if host in self.allowed_hosts:
            try:
                result = await asyncio.create_subprocess_exec('ping', '-c', '1', host, capture_output=True, text=True)
                return {'status': 'completed', 'output': result.stdout}
            except subprocess.CalledProcessError as e:
                return {'status': 'error', 'message': str(e)}
        else:
            return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping_instance.ping(host)