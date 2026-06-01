from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def ping(host: str):
        try:
            result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingCommand.ping(host)