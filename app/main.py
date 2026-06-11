from fastapi import FastAPI
import subprocess
def escape_host(host):
    host = host.replace(';', '').replace('&', '').replace('|', '').replace('(', '').replace(')', '')
    return host
class SafeFastAPI:
    def __init__(self, app):
        self.app = app
    async def ping(self, host: str):
        safe_host = escape_host(host)
        subprocess.run(['ping', '-c', '1', safe_host], check=True)
app = FastAPI()
safe_app = SafeFastAPI(app)
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_safe(request):
    host = request.query_params.get('host', '')
    return safe_app.ping(host)