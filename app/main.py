from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)