from fastapi import FastAPI
import subprocess
class PingService:
    def ping(self, host: str):
        try:
            result = subprocess.run(['ping', '-c', '1', subprocess.check_output('echo %s' % host, shell=True).decode().strip()], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingService().ping(host)