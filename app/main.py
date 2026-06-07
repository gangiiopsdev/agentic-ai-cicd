from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        result = subprocess.call(args)
        return result

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = PingCommand.safe_ping(host)
    return {'status': 'completed', 'result': result}