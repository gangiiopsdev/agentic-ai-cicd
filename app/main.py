from fastapi import FastAPI
import subprocess
import shlex
class SanitizeInputMiddleware:
    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http' and scope['path'].startswith('/ping'):
            query_params = scope['query_string'].decode('utf-8').split('&')
            host_param = next((param for param in query_params if param.startswith('host=')), None)
            host = '' if not host_param else shlex.quote(host_param.split('=')[1])
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