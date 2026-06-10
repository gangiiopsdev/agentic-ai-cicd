from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping'] + shlex.split(host), shell=False, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService().ping(host)