from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str):
        command = ['ping', *shlex.split(host)]
        try:
            output = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

db_service = PingService()

@app.get("/ping")
def ping(host: str):
    return db_service.ping(host)