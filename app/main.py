from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'output': str(e.output)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    command_instance = PingCommand()
    return command_instance.ping(host)