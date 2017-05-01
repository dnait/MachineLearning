import subprocess
subprocess.call(["ls", "-l"])
subprocess.check_output(
    "ls non_existent_file; exit 0",
    stderr = subprocess.STDOUT,
    shell=True)


p = subprocess.Popen(["echo", "hi Apple"], stdout=subprocess.PIPE)
print p.communicate()

p = subprocess.Popen(["mkdir", "myfolder"], stdout=subprocess.PIPE)
subprocess.call(["ls", "-l"])
print p.communicate()

#Ping program using subprocess
host = raw_input("Enter a host to ping:")
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)
output = p1.communicate()[0]
print output

