from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    def __init__(self, args):
        self.args = args

    def run(self, *args):
        full_args = [shlex.quote(arg) for arg in self.args]
        subprocess.run(full_args + list(args), check=True, timeout=5)

class PingEndpoint:
    def __init__(self, app: FastAPI):
        self.app = app

    @app.get("/ping")
    async def ping(self, host: str):
        safe_host = SafeSubprocess(['ping']).run(host)
        return {"status": "completed"}

app = FastAPI()
ping_endpoint = PingEndpoint(app)