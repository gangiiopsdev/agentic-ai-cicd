from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Validate and sanitize the input
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        return None
    
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class App:
    def __init__(self):
        self.app = FastAPI()
    @app.get('/')
    def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}
    @app.get('/ping')
    async def ping(self, host: str):
        # Validate and sanitize the input
        if safe_ping(host) is None:
            return {'error': 'Invalid hostname'}, 400
        return {'result': safe_ping(host)}
class Main:
    @staticmethod
def main():
        app = App().app
        import uvicorn
        uvicorn.run(app, host='127.0.0.1', port=8000)
Main.main()