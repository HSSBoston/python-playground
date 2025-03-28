import subprocess

command = "aplay violin4.wav"

subprocess.run(command, shell=True)
