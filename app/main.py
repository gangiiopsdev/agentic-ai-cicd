from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Using subprocess.Popen instead of subprocess.call and avoiding shell=True
        args = ['ping', self.host]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode(), error.decode()

global ping_command
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global ping_command
    if not ping_command:
        ping_command = PingCommand(host)
    output, error = ping_command.execute()
    return {'status': 'completed', 'output': output, 'error': error}