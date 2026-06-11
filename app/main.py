from fastapi import FastAPI
import subprocess
import shlex

class PingHandler:
    @staticmethod
def safe_ping(host: str) -> bool:
        command = ['ping', host]
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f'Error pinging {host}: {e}')
            return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler()
    if handler.safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}