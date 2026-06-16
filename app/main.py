from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input
    if host.isalnum() and '.' in host:
        args = ['ping', host]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'status': 'completed'}
    else:
        return {'status': 'invalid_host'}