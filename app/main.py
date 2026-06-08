from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    service = PingService()
    return service.ping(host)