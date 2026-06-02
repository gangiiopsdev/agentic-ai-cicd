from fastapi import FastAPI
import subprocess
gluster_command = ['ping', host]
subprocess.call(gluster_command)