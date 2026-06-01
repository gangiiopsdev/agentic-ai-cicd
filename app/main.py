from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return output

@app.get("/ping")
async def ping(host: str):
    try:
        response = await safe_ping(host)
        return {"status": "completed", "response": response.decode()}
    except ValueError as e:
        return {"status": "error", "message": str(e)}