from fastapi import FastAPI
import subprocess
def escape_shell(command):
    return command.replace(';', '').replace('&', '').replace('|', '')

class PingService:
    @staticmethod
def ping(host: str):
        escaped_host = escape_shell(host)
        try:
            output = subprocess.run(['ping', '-c', '1', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': output.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/ping')
def ping_wrapper(host: str):
    return PingService.ping(host)