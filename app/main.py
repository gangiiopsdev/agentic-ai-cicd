from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> str:
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not all(c.isalnum() or c in ('-', '.') for c in host):
        raise ValueError('Invalid hostname')
    command = PingCommand(host)
    output = command.execute()
    return {'status': 'completed', 'output': output}