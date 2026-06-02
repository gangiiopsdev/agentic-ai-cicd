from fastapi import FastAPI
import subprocess
call_args = ['ping', host]
subprocess.call(call_args)