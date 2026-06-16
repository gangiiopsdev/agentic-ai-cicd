from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run instead of shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class App:
    def __init__(self):
        self.app = FastAPI()
        self.app.get('/', endpoint=self.home)
        self.app.get('/ping', endpoint=lambda request: self.ping(request.query_params['host']))

    def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}

    def ping(self, host: str):
        return safe_ping(host)

app = App().app