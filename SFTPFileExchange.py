import paramiko


def establish_connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="127.0.0.1", username="test_user", password="test", port=22)
    return ssh


def get_sftp_client(ssh):
    return ssh.open_sftp()


def close_connection(ssh, sftp_client):
    sftp_client.close()
    ssh.close()


def transfer_file(remote_file_path, local_file_path):
    ssh = establish_connection()
    sftp_client = get_sftp_client(ssh)
    sftp_client.put(
        r"{}".format(local_file_path),
        r"{}".format(remote_file_path),
    )
    close_connection(ssh, sftp_client)


def download_file(local_file_path, remote_file_path):
    ssh = establish_connection()
    sftp_client = get_sftp_client(ssh)
    sftp_client.put(
        r"{}".format(remote_file_path),
        r"{}".format(local_file_path),
    )
    close_connection(ssh, sftp_client)
