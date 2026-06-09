from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        pass

    async def ping(self, host: str):
        try:
            # Safe implementation using subprocess.run with shell=False and args parameter
            subprocess.call(['ping', host])
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    ping_instance = Ping()
    return ping_instance.ping(host)