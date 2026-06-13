from fastapi import FastAPI
import subprocess
import shlex
def safe_call_process(command, *args):
    sanitized_command = shlex.quote(command)
    sanitized_args = [shlex.quote(arg) for arg in args]
    return subprocess.run([sanitized_command] + sanitized_args, check=True, capture_output=True)
call_process = safe_call_process