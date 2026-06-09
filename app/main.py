from fastapi import FastAPI
import subprocess
globals = {
    'ping': ['google.com', '127.0.0.1']
}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in globals['ping']:
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid input')