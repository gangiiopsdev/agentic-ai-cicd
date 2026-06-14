from fastapi import FastAPI
import subprocess
import shlex
class SafeCommandRunner:
    def __init__(self):
        self.safe_commands = ['ping']

    def safe_run(self, command, args=None):
        if command in self.safe_commands:
            if args:
                return subprocess.check_output([command] + shlex.split(args), stderr=subprocess.STDOUT, timeout=5)
            else:
                return subprocess.check_output([command], stderr=subprocess.STDOUT, timeout=5)
        else:
            raise ValueError(f"Unsafe command: {command}")

app = FastAPI()
sr = SafeCommandRunner()
def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

def escape_args(args):
    return ' '.join(shlex.quote(arg) for arg in args)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = sr.safe_run('ping', f'-c 1 {shlex.quote(sanitized_host)}')
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode('utf-8')}