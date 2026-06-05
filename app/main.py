from fastapi import FastAPI
import subprocess
import shlex
class CommandExecutor:
    @staticmethod
def execute(command: str, *args):
        full_command = [command] + list(args)
        result = subprocess.run(full_command, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    result = CommandExecutor.execute('ping', safe_host)
    return {'status': 'completed', 'result': result}