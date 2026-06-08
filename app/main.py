from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        cmd = ['ping', host]
        args = shlex.split(' '.join(cmd))
        try:
            result = subprocess.run(args, check=True, shell=False)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)