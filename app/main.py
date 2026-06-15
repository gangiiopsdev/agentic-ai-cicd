from fastapi import FastAPI
import subprocess

allowed_hosts = ['google.com', 'bing.com']

async def safe_ping(host: str):
    if host in allowed_hosts:
        try:
            output = await asyncio.create_subprocess_exec('ping', '-c', '4', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await output.communicate()
            return {'status': 'completed', 'output': stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return await safe_ping(host)