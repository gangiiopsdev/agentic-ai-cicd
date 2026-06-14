from fastapi import FastAPI
import subprocess
class SecurePing:
    @staticmethod
def ping(host: str):
        try:
            # Use check_output to capture the output and ensure it completes successfully
            result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': result}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return SecurePing.ping(host)