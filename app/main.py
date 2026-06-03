from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return shlex.quote(arg)

cmd = ['ping', escape_shell_arg(host)]
result = subprocess.run(cmd, capture_output=True, text=True)
return {'status': 'completed', 'output': result.stdout}