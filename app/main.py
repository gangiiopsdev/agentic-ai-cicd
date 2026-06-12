from fastapi import FastAPI
import subprocess
global host = 'example.com'

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_host():
    return ping(global host)