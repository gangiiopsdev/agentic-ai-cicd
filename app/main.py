from fastapi import FastAPI
import subprocess
cimport = ['ping']

cdef = host:
    result = subprocess.run(cimport + [host], capture_output=True, text=True)
    return result.stdout