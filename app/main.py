from fastapi import FastAPI
import shlex

class SafeFastAPI:
    def __init__(self, app):
        self.app = app
    async def ping(self, host: str):
        if not all(c.isalnum() or c in '-.' for c in host):
            raise ValueError('Invalid characters in hostname')
        command = ['ping', '-c', '1'] + shlex.split(host)
        subprocess.run(command, check=True)

app = FastAPI()
safe_app = SafeFastAPI(app)
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_safe(request):
    host = request.query_params.get('host', '')
    return safe_app.ping(host)