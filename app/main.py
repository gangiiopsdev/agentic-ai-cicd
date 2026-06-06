from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self):
        self.command_list = ['ping', 'traceroute']

    def execute_command(self, cmd):
        if cmd in self.command_list:
            subprocess.run(cmd.split(), check=True)
        else:
            raise ValueError('Invalid command')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    executor = CommandExecutor()
    try:
        executor.execute_command(f'ping {host}')
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 400