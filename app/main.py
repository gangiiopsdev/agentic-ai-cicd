from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.host = None

    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    result = ping_service.ping(host)
    return {'status': 'completed', 'result': result}