from fastapi import FastAPI
import subprocess

global app = FastAPI()

async def ping(host: str):
    # Safe implementation using subprocess.run and avoiding shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}