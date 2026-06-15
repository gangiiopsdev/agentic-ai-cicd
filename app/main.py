from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Validate the host input to prevent command injection
    if not host.strip() or '@' in host or ' ' in host:
        raise ValueError('Invalid host input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = await safe_ping(host)
    return {"status": "completed", "response": response}