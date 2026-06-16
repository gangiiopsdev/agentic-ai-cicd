from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    args = ['ping', host]
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        response = await safe_ping(host)
        return {"status": "completed", "response": response}
    except Exception as e:
        return {"status": "error", "message": str(e)}