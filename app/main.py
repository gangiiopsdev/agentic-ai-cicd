from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    response = safe_ping.execute()
    return {'status': 'completed', 'response': response}