from fastapi import FastAPI
import subprocess
class CommandExecution:
    def __init__(self, args):
        self.args = args

def execute_command(command_instance):
    return subprocess.call(command_instance.args)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = ['ping', host]
    command_instance = CommandExecution(args)
    result = execute_command(command_instance)
    return {'status': 'completed', 'result': result}