from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping_safe(host: str):
    try:
        output = await asyncio.to_thread(subprocess.run, ['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': await ping_safe(host)}