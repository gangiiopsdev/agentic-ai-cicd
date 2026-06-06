from fastapi import FastAPI
import subprocess
g
app = FastAPI()

def ping(host: str):
    # Safer implementation
    subprocess.call(['ping', host])

@app.get="/ping")
def ping_safe(host: str):
    return {'status': 'completed'}