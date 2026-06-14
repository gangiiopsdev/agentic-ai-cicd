from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

class PingEndpoint:
    @staticmethod
    def get(host: str):
        service = PingService()
        return service.ping(host)

@app.get("/ping")
def ping(host: str):
    endpoint = PingEndpoint()
    return endpoint.get(host)