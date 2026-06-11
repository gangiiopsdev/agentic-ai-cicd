from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    # Add your input sanitization logic here
    return ''.join(c for c in input_string if c.isalnum() or c in [',', '-', '.'])

class SafeSubprocess:
    @staticmethod
def execute_command(command, args):
        try:
            result = subprocess.run([command] + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.output}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    return SafeSubprocess.execute_command(command, [])