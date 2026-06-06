from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if host.strip() and all(c.isalnum() for c in host):
        try:
            output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = await output.wait()
            return result.returncode == 0
        except Exception as e:
            return False

@app.get("/ping")
def get_ping_status():
    return {"status": "completed"}