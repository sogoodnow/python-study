import paramiko

trassport = paramiko.Transport("192.168.204.128",22)
trassport.connect(username="root",password="root")