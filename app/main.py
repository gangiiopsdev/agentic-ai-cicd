from fastapi import FastAPI
import subprocess
def safe_call_process(command, *args):
    return subprocess.run([command] + list(args), check=True, capture_output=True)
call_process = safe_call_process