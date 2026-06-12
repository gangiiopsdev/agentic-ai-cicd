from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Safe implementation without shell=True
    try:
        result = await asyncio.create_subprocess_exec('ping', '-c', '1', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise Exception(f'Ping failed: {error.decode()}')
        return output
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}