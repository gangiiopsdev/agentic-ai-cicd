from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def safe_execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, shell=False)
            return True, output.decode()
        except subprocess.CalledProcessError as e:
            return False, e.output.decode()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing(host)
    success, result = safe_ping_instance.safe_execute()
    if success:
        return {"status": "completed", "output": result}
    else:
        return {"status": "failed", "error": result}