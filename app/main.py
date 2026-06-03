from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    if isinstance(arg, list):
        return ' '.join(escape_shell_arg(a) for a in arg)
    elif ' ' in arg or '	' in arg or '&' in arg or ';' in arg or '>' in arg or '<' in arg:
        return f'"{arg}"'
    else:
        return arg
class SafeSubprocess:
    @staticmethod
    def call(command, **kwargs):
        if isinstance(command, str):
            command = command.split()
        args = [escape_shell_arg(arg) for arg in command]
        subprocess.call(args, **kwargs)
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate against a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host name'}
    SafeSubprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}