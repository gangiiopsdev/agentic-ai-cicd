from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, shell=False, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen with proper arguments
    command = PingCommand(['ping', host])
    return {'status': 'completed'}