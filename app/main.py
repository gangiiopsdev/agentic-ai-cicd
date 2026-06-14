from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        try:
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return {'status': 'completed', 'stdout': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'stderr': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)