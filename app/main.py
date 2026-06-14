from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str):
        command = ['ping', host]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'status': 'completed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    return ping_service.ping(host)