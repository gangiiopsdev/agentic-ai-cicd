from fastapi import FastAPI
import subprocess
import shlex

class SafeCommandExecutor:
    @staticmethod
def execute_command(command, *args):
        try:
            result = subprocess.run([command] + list(shlex.split(' '.join(args))), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    executor = SafeCommandExecutor()
    return executor.execute_command('ping', sanitized_host)