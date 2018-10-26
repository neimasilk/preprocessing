import subprocess
import shlex

subprocess.call(shlex.split(
    "proxybroker find --types HTTP --lvl High --countries US CA FR GB DE SG --strict -l 100 -o ./proxies.txt"))
# subprocess.call(shlex.split("mv working_proxy.txt working_proxy%s.txt" % 100))
subprocess.call(shlex.split("python proxy_finder.py"))
