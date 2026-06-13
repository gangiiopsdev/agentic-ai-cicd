from fastapi import FastAPI
import subprocess
def validate_host(host):
    return all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host)

class PingCommand:
    def __init__(self, host):
        if not validate_host(host):
            raise ValueError('Invalid input')
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, text=True)
            return output
        except subprocess.CalledProcessError as e:
            return str(e.output)

app = FastAPI()

def execute_ping(host):
    return PingCommand(host).execute()

@app.get('/ping')
def ping(host: str):
    result = execute_ping(host)
    return {'status': 'completed', 'result': result}