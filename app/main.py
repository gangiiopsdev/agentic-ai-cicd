from fastapi import FastAPI
import subprocess
class PingEndpoint:
    def __init__(self, app: FastAPI):
        self.app = app

    @app.get("/ping")
    async def ping(self, host: str):
        try:
            result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, timeout=5, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()
ping_endpoint = PingEndpoint(app)