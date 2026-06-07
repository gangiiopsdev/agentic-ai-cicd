from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
class SafePingMiddleware:
    async def __call__(self, call_next):
        request = await call_next()
        if request.url.path == '/ping':
            host = request.query_params.get('host', '')
            if not all(c.isalnum() for c in host) and host != 'localhost':
                raise ValueError('Invalid host name')
        return request

app = FastAPI(middleware=[SafePingMiddleware()])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}