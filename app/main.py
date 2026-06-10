from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        # Validate or sanitize the host input
        if not host.isalnum():
            raise ValueError('Invalid host name')
        args = ['ping', shlex.quote(host)]
        result = await subprocess.run(args, capture_output=True, text=True)
        return result.stdout

safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    output = safe_ping_instance.ping(host)
    return {"status": "completed", "output": output}