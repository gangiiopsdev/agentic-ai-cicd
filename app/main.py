from fastapi import FastAPI
import subprocess
class CommandRunner:
    @staticmethod
def run_command(command: str):
        try:
            result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    return CommandRunner.run_command(command)