from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():  # Simple check to prevent command injection
        return {'error': 'Invalid input'}
    try:
        subprocess.run(['ping', self.host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}