from fastapi import FastAPI
import shlex
def safe_ping(host: str):
    # Sanitize the input to avoid shell injection
    host = shlex.quote(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return result.stdout
class PingRouter:
    def __init__(self):
        self.app = FastAPI()
        self.register_routes()
    def register_routes(self):
        @self.app.get("/ping")
        async def ping(host: str):
            try:
                output = safe_ping(host)
                return {'status': 'completed', 'output': output}
            except subprocess.CalledProcessError as e:
                return {'status': 'error', 'message': str(e)}
ping_router = PingRouter().app