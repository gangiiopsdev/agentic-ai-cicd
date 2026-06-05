from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Fixed implementation
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return f'Error: {error.decode()}'
        return output.decode()
    except Exception as e:
        return f'Error: {e}''

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)