import subprocess 
import datetime

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
print("================================")
print("System Health Check: " + timestamp)
print("================================")

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

cpu_load = run_command("uptime | awk -F'load average:' '{print $2}'")
print("CPU Load: " + cpu_load)

memory = run_command("free -h | grep Mem | awk '{print $3 \" used of \" $2}' ")
print("Memory: " + memory)

disk = run_command("""df -h / | tail -1 | awk '{print $3 " used of " $2 " (" $5 ")"}'""")
print("Disk: " + disk)

# Apache
apache = run_command("systemctl is-active apache2")
print("Apache: " + apache)

# Network
http_code = run_command("curl -s -o /dev/null -w '%{http_code}' http://google.com")
print("Internet: HTTP " + http_code)

print("=================================")
