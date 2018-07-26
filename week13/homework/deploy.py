import paramiko

# 服务器定义
IP = "192.168.119.147"
USER = "root"
PASSWORD = "root"
PORT = 22

transport = paramiko.Transport(IP,PORT)
transport.connect(username=USER,password=PASSWORD)
sftp = paramiko.SFTPClient.from_transport(transport)
# 爬虫项目上传
sftp.put("./W10csdnMS.zip","/root/W10csdnMS.zip")
sftp.put("./W10csdnS1.zip","/root/W10csdnS1.zip")
sftp.close()
transport.close()
# 通过paramokio进行解压
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname=IP,username=USER,password=PASSWORD,port=PORT)

command = "unzip /root/W10csdnMS.zip && unzip /root/W10csdnS1.zip"
stdin,stdout,stderr =ssh.exec_command(command)
print(stdout.read().decode())

command = "docker images|awk '/^redis/ {print $1}'"
stdin1,stdout1,stderr1 =ssh.exec_command(command)
if (stdout1.read().decode())=="":
    command = "docker pull redis"
    stdin2, stdout2, stderr2 = ssh.exec_command(command)
    print(stdout2.read().decode())




ssh.close()