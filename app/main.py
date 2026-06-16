from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    def __init__(self, command: list):
        self.command = command

    def run(self):
        try:
            result = subprocess.run(self.command, capture_output=True, check=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

global_safe_subprocess = SafeSubprocess(['ping', '{host}'])

def ping(host: str):
    global_safe_subprocess.command[1] = host
    return {'status': 'completed'}