from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            args = ['ping'] + shlex.split(host)
            subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)