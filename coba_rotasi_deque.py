import subprocess
import shlex

r = subprocess.call(shlex.split("python wiki_get_sentence.py"))

print("selesai")
