from fastapi import FastAPI
import subprocess
glitchfix = FastAPI()

@glitchfix.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True, text=True)

return {'status': 'completed'}