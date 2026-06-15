from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Use check_output instead of call for safer execution
        try:
            result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': result.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.safe_ping(host)