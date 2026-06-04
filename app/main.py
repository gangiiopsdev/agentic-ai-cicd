from fastapi import FastAPI
import subprocess
def ping_host(host):
    # Ensure host input is sanitized
    sanitized_host = subprocess.shlex.quote(host)
    git = subprocess.Popen(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = git.communicate()
    return {'status': 'completed'}