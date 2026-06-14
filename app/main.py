from fastapi import FastAPI
import subprocess
class CommandRunner:
    @staticmethod
def run_command(command: str):
        # Validate and sanitize the command input
        allowed_commands = ['ping']
        if command.split()[0] in allowed_commands:
            try:
                result = subprocess.run(command.split(), capture_output=True, check=True, text=True)
                return result.stdout
            except subprocess.CalledProcessError as e:
                return f"Command failed with error: {e.stderr}"
        else:
            return 'Invalid command'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    output = CommandRunner.run_command(' '.join(command))
    return {'status': 'completed', 'output': output}