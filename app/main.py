from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if host.strip() and all(c.isalnum() for c in host):
        args = ['ping', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return output.decode('utf-8'), error.decode('utf-8') if error else None
    else:
        return None

@app.get("/ping")
def get_ping_status():
    return {"status": "completed"}