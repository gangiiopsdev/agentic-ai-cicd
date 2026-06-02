from fastapi import FastAPI
import subprocess
def ping_host(host):
    # Validate and sanitize the host input
    if not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError('Invalid host parameter')
    cimport = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = cimport.communicate()
    return output.decode(), error.decode()