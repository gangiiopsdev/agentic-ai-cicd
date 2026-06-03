from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafeFastAPI:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/')
    def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}

    @app.get('/ping')
    def ping(self, host: str):
        return safe_ping(host)
safe_app = SafeFastAPI().app