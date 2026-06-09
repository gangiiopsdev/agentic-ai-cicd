from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()
cping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return cping_service.ping(host)