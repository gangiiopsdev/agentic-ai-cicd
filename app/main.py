from fastapi import FastAPI
import subprocess

app = FastAPI()

async def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, args, output=output, stderr=error)
    except Exception as e:
        raise RuntimeError(f'Ping failed: {e}')

@app.get("/ping")
def ping(host: str):
    try:
        await run_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}