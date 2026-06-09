from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        output = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

cmd = ['ping', host]
execute_command(cmd)