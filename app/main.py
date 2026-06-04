from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    output = SafePing.ping(host)
    return {"status": "completed", "output": output}