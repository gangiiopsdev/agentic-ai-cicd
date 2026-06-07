from fastapi import FastAPI
import shlex

class CommandExecutor:
    @staticmethod
def execute(command: str, *args):
        full_command = [command] + list(args)
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    try:
        result = CommandExecutor.execute('ping', '-c 1', safe_host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    return {'status': 'completed', 'result': result}