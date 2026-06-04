from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return SafeSubprocess.ping(host)