from fastapi import FastAPI
import subprocess
class PingService:
    def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return output.decode('utf-8'), 0
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8'), e.returncode

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result, exit_code = PingService.ping(host)
    if exit_code == 0:
        return {'status': 'completed', 'result': result}
    else:
        return {'status': 'failed', 'result': result}