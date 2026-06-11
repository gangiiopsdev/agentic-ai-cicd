from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

class Ping:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        # Validate and sanitize the input to prevent command injection
        if not host.strip().replace('.', '').isdigit():
            return {'status': 'error', 'message': 'Invalid host'}
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

if __name__ == '__main__':
    ping_instance = Ping()
    import uvicorn
    uvicorn.run(ping_instance.app, host='127.0.0.1', port=8000)