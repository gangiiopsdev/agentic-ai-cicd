from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = subprocess.quote(host)
        try:
            result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    return SafePing.ping(host)