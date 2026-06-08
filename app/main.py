from fastapi import FastAPI
import subprocess
class Ping:
    @staticmethod
def run(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = Ping.run(host)
    return {"status": "completed", "output": output}