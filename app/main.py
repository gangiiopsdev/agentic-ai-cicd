from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

class PingRouter:
    @staticmethod
def ping_route(host: str):
        service = PingService()
        return service.ping(host)

app = FastAPI()

@app.get("/ping")
def ping_router(host: str):
    router = PingRouter()
    return router.ping_route(host)