import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="127.0.0.1", username="test_user", password="test", port=22)
sftp_client = ssh.open_sftp()
sftp_client.chdir("/folder")
print(sftp_client.getcwd())

# downloading sftp server's file to local
sftp_client.get(
    "/folder/abc.xlsx",
    "D:\Robi Work 2021\File Handling Algorithm/abc.xlsx",
)
# transferring local file to sftp
sftp_client.put(
    r"D:\Entertainment\Downloads\abc.xlsx",
    "/folder/abc.xlsx",
)

sftp_client.close()
ssh.close()