from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            args = ['ping'] + host.split(' ')
            response = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': response.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)