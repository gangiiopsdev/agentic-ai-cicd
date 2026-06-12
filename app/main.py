from fastapi import FastAPI
import subprocess

async def safe_ping(host):
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()
    except Exception as e:
        return f'Error: {e.stderr.decode()}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    response = await safe_ping(host)
    return {'status': 'completed', 'response': response.decode() if isinstance(response, tuple) else response}