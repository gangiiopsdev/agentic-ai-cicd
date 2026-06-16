from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            subprocess.call(['ping', self.host])
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    if result['status'] == 'error':
        return {'status': 'completed', 'message': result['message']}
    return {'status': 'completed'}