from fastapi import FastAPI
import httpx
get_running_loop = asyncio.get_running_loop

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.startswith('http://localhost') and not host.startswith('https://localhost'):
        raise ValueError('Invalid host')
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://{host}/ping')
    return {'status': 'completed', 'response': response.text}