from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.safe_hosts = ['google.com', 'github.com']

    async def ping(self, host: str) -> dict:
        if host not in self.safe_hosts:
            return {'status': 'not allowed'}
        args = ['ping', shlex.quote(host)]
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)