from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        # Use the correct method to avoid shell=True
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', output=output, stderr=error)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return await ping(host)