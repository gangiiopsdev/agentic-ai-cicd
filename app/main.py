from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise Exception(f'Ping failed: {error.decode()}')
        return {'output': output.decode()}
    except Exception as e:
        return {'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)