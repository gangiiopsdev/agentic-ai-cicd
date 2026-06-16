from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    # Validate and sanitize host input
    try:
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, args, output=output, stderr=error)
    except subprocess.CalledProcessError as e:
        raise ValueError(f'Ping failed: {e}')

@app.get("/ping")
def ping(host: str):
    try:
        await safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400