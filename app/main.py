from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', self.host], timeout=5)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}