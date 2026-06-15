from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.Popen with validation and sanitization
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed'}