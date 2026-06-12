from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', self.host], stderr=subprocess.STDOUT)
            return output.decode()
        except subprocess.CalledProcessError as e:
            return e.output.decode() + str(e.returncode)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {'status': 'completed', 'result': result}