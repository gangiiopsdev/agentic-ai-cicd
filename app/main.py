from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    try:
        output = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}