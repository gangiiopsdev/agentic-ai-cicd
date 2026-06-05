from fastapi import FastAPI
import subprocess

app = FastAPI()

async def _ping(host):
    try:
        output = await asyncio.to_thread(subprocess.check_output, ['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output.decode('utf-8'))

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'result': _ping(host)}