from fastapi import FastAPI
import subprocess
from shlex import quote
class PingCommand(subprocess.Popen):
    def __init__(self, host: str):
        super().__init__(['ping', '-c', '1', quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = PingCommand(host)
    return {'status': 'completed', 'output': result.stdout}