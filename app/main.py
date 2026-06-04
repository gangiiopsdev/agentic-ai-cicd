from fastapi import FastAPI
import os
import shlex
class SafeCommandRunner:
    def __init__(self, command):
        self.command = command

    def run(self):
        try:
            result = subprocess.run(self.command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if all(char in allowed_chars for char in host):
        return True
    return False
@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        command = ['ping', shlex.quote(host)]
        runner = SafeCommandRunner(command)
        output = runner.run()
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid host"}