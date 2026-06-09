from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate the host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[0-9a-zA-Z.-]+$', host):
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
async def ping(host: str):
    return await asyncio.to_thread(ping, host)