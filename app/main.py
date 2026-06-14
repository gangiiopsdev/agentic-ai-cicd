from fastapi import FastAPI
import subprocess
import shlex

class SanitizeInputMiddleware:
    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http' and scope['path'].startswith('/ping'):
            host = scope['query_string'].decode('utf-8').split('=')[1]
            host = shlex.quote(host)
        else:
            host = ''
        await self.app(scope, receive, send)

app = FastAPI(middleware=[SanitizeInputMiddleware()])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}