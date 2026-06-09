from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def safe_ping(self):
        try:
            output = subprocess.run(['ping', self.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return output.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.stderr.decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing(host)
    result = safe_ping_instance.safe_ping()
    return {"status": "completed", "result": result}