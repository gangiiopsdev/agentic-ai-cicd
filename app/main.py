from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    # Safe implementation using subprocess.run with shell=False and list of arguments
    args = ['ping', host]
    result = await asyncio.to_thread(subprocess.run, args, check=True)
    return result

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}