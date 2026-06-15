from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(subprocess.check_output(['echo', host]).decode('utf-8').strip())  # Ensure the input is safe
    output = command_executor.execute()
    return {'status': 'completed', 'output': output}