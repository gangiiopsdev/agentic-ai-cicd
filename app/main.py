from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum():
        return 'Invalid hostname'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    return {'status': await safe_ping(host)}