from fastapi import FastAPI
import subprocess

async def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        args = ['ping', '--', host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {"status": "completed", "output": output.decode('utf-8')}
    else:
        return {"status": "error", "message": "Host not allowed"}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)