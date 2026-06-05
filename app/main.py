from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['google.com', 'example.com']

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError("Invalid host")
        args = shlex.split('ping ' + host)
        result = await subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping_instance.ping(host)
    except ValueError as e:
        return {"status": "failed", "error": str(e)}