from fastapi import FastAPI
import asyncio
import subprocess

async def ping(host: str):
    try:
        result = await asyncio.to_thread(subprocess.run, ['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode()}