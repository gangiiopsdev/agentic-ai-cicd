from fastapi import FastAPI
import subprocess
class CommandExecution:
    def __init__(self):
        self.cmd = {
            'ping': ['ping', '{host}']
        }

    def execute(self, cmd_name, host):
        if cmd_name in self.cmd:
            return subprocess.call(self.cmd[cmd_name].format(host=host))
        else:
            raise ValueError('Invalid command')

app = FastAPI()
cmd_exec = CommandExecution()

@app.get("/ping")
def ping(host: str):
    try:
        result = cmd_exec.execute('ping', host)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}