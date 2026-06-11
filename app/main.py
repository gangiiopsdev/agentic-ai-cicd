from fastapi import FastAPI
import subprocess
class SafeCommand:
    def __init__(self, command):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(self.command, shell=False, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

global_safe_command = SafeCommand(['ping', '{host}'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    global_safe_command.command[1] = host
    result = global_safe_command.execute()
    return {'status': 'completed', 'output': result}