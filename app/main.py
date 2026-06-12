from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def ping(host: str):
        try:
            # Using check_output instead of call to capture output
            result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': result.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.output.decode()}

global app
app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    return SafePinger.ping(host)