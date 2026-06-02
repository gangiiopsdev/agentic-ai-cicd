from fastapi import FastAPI
import subprocess
import shlex

class CommandExecutor:
    @staticmethod
def execute(command: str, *args):
        try:
            result = subprocess.run([command] + shlex.split(' '.join(args)), check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed with error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    executor = CommandExecutor()
    output = executor.execute('ping', host)
    return {'status': 'completed', 'output': output}