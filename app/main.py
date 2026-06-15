from fastapi import FastAPI
import subprocess
import shlex
import os
import tempfile
class CommandSanitizer:
    @staticmethod
def sanitize_command(command_parts):
        return [shlex.quote(part) for part in command_parts]
app = FastAPI()
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() and e.isprintable())
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    with tempfile.TemporaryDirectory() as temp_dir:
        command = CommandSanitizer.sanitize_command(['/bin', 'ping', sanitized_host])
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True, cwd=temp_dir, shell=False)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}