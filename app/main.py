from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def safe_ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE)
    return await result.communicate()

@app.get("/ping")
def ping(host: str):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        output = loop.run_until_complete(safe_ping(host))
        return {"status": "completed", "output": output[0].decode()}
    finally:
        loop.close()