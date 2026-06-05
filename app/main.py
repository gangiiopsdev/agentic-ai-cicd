from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host: str):
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode == 0:
            return {'status': 'completed', 'output': output.decode()}
        else:
            return {'status': 'failed', 'error': error.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return run_ping(host)