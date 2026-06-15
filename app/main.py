from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead and avoid shell=True
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

class PingRouter:
    @staticmethod
    def ping(host: str):
        return {'status': 'completed', 'output': safe_ping(host)}

app.include_router(PingRouter, tags=['ping'])