from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return output.decode('utf-8')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)