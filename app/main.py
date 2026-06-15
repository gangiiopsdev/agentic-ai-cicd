from fastapi import FastAPI
import subprocess
generate_command = ['ping', host]
subprocess.call(generate_command)