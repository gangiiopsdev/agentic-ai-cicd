from fastapi import FastAPI
import subprocess
cimport os
cdef ping(host: str):
    # Secure implementation using os.system
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}