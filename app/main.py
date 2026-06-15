from fastapi import FastAPI
import subprocess
class CommandExecution:
    def __init__(self, args):
        self.args = args

def execute_command(command_instance):
    return subprocess.run(command_instance.args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = ['ping', host]
    command_instance = CommandExecution(args)
    try:
        result = execute_command(command_instance)
        return {'status': 'completed', 'result': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}