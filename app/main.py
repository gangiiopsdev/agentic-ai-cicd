from fastapi import FastAPI
import subprocess
class PingException(Exception):
    pass

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise PingException("Invalid hostname")
    subprocess.call(['ping', host])
    return {"status": "completed"}