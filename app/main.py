from fastapi import FastAPI
import shlex
from subprocess import Popen, PIPE

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    args = shlex.split('ping ' + host)
    process = await asyncio.to_thread(Popen, args, stdout=PIPE, stderr=PIPE)
    output, error = await process.communicate()
    return output.decode(), error.decode()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = ping(host)
        return {"status": "completed", "output": result[0]}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}