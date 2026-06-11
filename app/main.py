from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    try:
        # Escape the host input to prevent command injection
        result = await asyncio.create_subprocess_exec('ping', subprocess.list2cmdline([host]), stdout=subprocess.PIPE)
        output, _ = await result.communicate()
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)