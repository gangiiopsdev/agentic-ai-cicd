from fastapi import FastAPI
import subprocess
class Ping:
    @staticmethod
def execute(host: str):
        args = ['ping', host]
        subprocess.run(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping()
    ping_instance.execute(host)
    return {"status": "completed"}