from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Validate input to prevent injection attacks
    if not isinstance(host, str) or len(host.strip()) == 0:
        return 'Invalid input'
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class SafePing:
    def __init__(self):
        self.safe_ping = safe_ping

    async def ping(self, host: str):
        try:
            output = await self.safe_ping(host)
            return {'status': 'completed', 'output': output}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing()
    return await safe_ping_instance.ping(host)