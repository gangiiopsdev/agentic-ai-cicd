from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def run_command(command: str, *args):
        full_command = [command] + list(shlex.split(' '.join(args)))
        try:
            result = subprocess.run(full_command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing()
    return safe_ping_instance.run_command('ping', host)