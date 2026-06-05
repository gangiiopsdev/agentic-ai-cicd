from fastapi import FastAPI
import subprocess
class PingHandler:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    handler = PingHandler()
    return handler.ping(host)