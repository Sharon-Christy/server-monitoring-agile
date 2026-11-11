import os

print("SERVER MONITORING APPLICATION")
print("-----------------------------")

print("CPU Usage:")
os.system("top -bn1 | grep 'Cpu(s)'")

print("\nMemory Usage:")
os.system("free -h")

print("\nDisk Usage:")
os.system("df -h /")

print("\nServer Monitoring Completed!")
