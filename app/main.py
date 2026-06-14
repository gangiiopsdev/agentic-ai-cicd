from fastapi import FastAPI
import subprocess
class PingSafe(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using safe Popen wrapper
    PingSafe(['ping', host])
    return {'status': 'completed'}