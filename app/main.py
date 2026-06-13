from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.command = ['ping', 'localhost']

app = FastAPI()

@app.get('/ping')
def ping():
    # Secure implementation with shell=False to prevent command injection
    ping_instance = PingCommand()
    subprocess.run(ping_instance.command, check=True, capture_output=True)

    return {'status': 'completed'}