from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        # Validate and sanitize input
        if not self.host.isalnum():
            raise ValueError('Invalid hostname')
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        command.execute()
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    return {"status": "completed"}