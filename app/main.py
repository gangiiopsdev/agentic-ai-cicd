from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Safe implementation
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')