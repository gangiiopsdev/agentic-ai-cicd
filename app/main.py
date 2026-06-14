from fastapi import FastAPI
import subprocess
class CommandRunner:
    def run(self, command: list):
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

cmd_runner = CommandRunner()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    output = cmd_runner.run(args)
    return {'status': 'completed', 'output': output}