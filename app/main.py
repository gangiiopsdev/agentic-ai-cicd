from fastapi import FastAPI
import subprocess
import shlex
class PingCommandBuilder:
    def __init__(self, host):
        self.host = host
        self.command = ['ping']

    def build_command(self):
        self.command.append(self.host)
        return self.command

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        builder = PingCommandBuilder(host)
        result = subprocess.run(builder.build_command(), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}