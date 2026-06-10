from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self):
        pass

    async def ping(self, host: str):
        try:
            # Safe implementation using subprocess.run with shell=False and args parameter
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'output': result.stdout}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    ping_instance = Ping()
    return ping_instance.ping(host)