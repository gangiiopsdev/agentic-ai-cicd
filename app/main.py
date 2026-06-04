from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safe implementation using subprocess.run and shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}