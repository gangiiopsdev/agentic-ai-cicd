from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise ValueError(f'Command failed with error: {e.stderr}')

class PingService:
    @staticmethod
def ping(host: str):
        if not host or len(host) > 255:
            raise ValueError('Invalid host name')
        command = ['ping', host]
        return SafeSubprocess.run(command)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    result = PingService.ping(host)
    return {'result': result}