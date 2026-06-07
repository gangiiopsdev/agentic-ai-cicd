from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.Popen with shell=False
        args = ['ping', self.host]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, error = process.communicate()
        return output.decode(), error.decode()
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output, error = command.execute()
    if error:
        return {'status': 'error', 'message': error}
    else:
        return {'status': 'completed', 'output': output}