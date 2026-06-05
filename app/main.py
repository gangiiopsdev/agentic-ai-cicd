from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation using subprocess.Popen
    command = 'ping {}
'.format(shlex.quote(host))
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed'}