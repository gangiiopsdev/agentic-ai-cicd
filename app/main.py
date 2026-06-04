from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
            return output
        except subprocess.CalledProcessError as e:
            return str(e.output)

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    result = SafeSubprocess.ping(host)
    return {'status': 'completed', 'result': result}