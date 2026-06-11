from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str):
        args = ['ping', host]
        subprocess.run(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    PingCommand.execute(host)
    return {"status": "completed"}