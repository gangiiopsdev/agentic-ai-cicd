from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.command = ['ping', 'localhost']

app = FastAPI()

@app.get('/ping')
def ping():
    # Secure implementation
    ping_instance = PingCommand()
    subprocess.call(ping_instance.command)

    return {'status': 'completed'}