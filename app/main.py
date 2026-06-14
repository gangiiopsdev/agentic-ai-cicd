from fastapi import FastAPI
import subprocess
import shlex
class PingEndpoint:
    def __init__(self, app: FastAPI):
        self.app = app

    @app.get("/ping")
    async def ping(self, host: str):
        try:
            # Validate and sanitize the input
            if not host.strip().isdigit():
                raise ValueError("Invalid host input")
            result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True, timeout=5, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except (subprocess.CalledProcessError, ValueError) as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()
ping_endpoint = PingEndpoint(app)