from fastapi import FastAPI
import subprocess
global allow_ping
allow_ping = True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global allow_ping
    if allow_ping and host in ["example.com", "test.com"]:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'denied'}