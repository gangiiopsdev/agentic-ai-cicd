from fastapi import FastAPI
import subprocess

class SafePing:
    def __init__(self):
        self.allowed_hosts = {'localhost', '127.0.0.1'}

    async def safe_ping(self, host):
        if host not in self.allowed_hosts:
            raise ValueError('Host is not allowed to ping')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    output = safe_ping_instance.safe_ping(host)
    return {"status": "completed", "output": output}