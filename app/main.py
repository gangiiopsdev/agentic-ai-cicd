from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    def __init__(self, command_parts):
        self.command_parts = command_parts

    def execute(self, *args):
        try:
            args = [part.format(*args) for part in self.command_parts]
            output = subprocess.check_output(args, universal_newlines=True, timeout=5)
            return {"status": "completed", "output": output}
        except Exception as e:
            return {"status": "failed", "error": str(e)}

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e == '.' or e == '-' or e == '_')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command_parts = ['ping', '{host}']
    safe_command = SafeCommand(command_parts)
    return safe_command.execute(host=sanitized_host)