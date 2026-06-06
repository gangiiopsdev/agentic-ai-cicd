from fastapi import FastAPI
import subprocess
import shlex

class SafePinger:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

# Usage
safe_pinger = SafePinger()
safe_pinger.app.include_router(safe_pinger.app.routes)