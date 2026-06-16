from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run_command(command: str, *args):
        safe_args = shlex.split(command)
        safe_args.extend(args)
        result = subprocess.run(safe_args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = 'ping'
    args = shlex.split(host)
    output = SafeSubprocess.run_command(command, *args)
    return {'status': 'completed', 'output': output}