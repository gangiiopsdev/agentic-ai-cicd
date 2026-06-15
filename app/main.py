from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

global_safe_ping = SafePing.safe_ping

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': global_safe_ping(host)}