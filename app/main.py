from fastapi import FastAPI
import subprocess
class PingHandler:
    @staticmethod
def run_ping(host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler()
    return handler.run_ping(host)