from fastapi import FastAPI
import subprocess
global_result = None
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

def execute_command(command, args):
    global global_result
    try:
        result = subprocess.run([command] + args, check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        global_result = {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        global_result = {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    execute_command('ping', [escaped_host])
    return global_result