from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping(host)
    result = ping_instance.execute()
    return {'status': 'completed', 'result': result}