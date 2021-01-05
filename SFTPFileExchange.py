import paramiko
from datetime import datetime
import logging

logging.basicConfig(
    filename="file.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def establish_connection(hostname, username, password, port):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password, port=port)
        return ssh
    except Exception as e:
        logging.error("SSH Connection Error - {}".format(e))


def establish_connection_local():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="127.0.0.1", username="test_user", password="test", port=22)
    return ssh


def get_sftp_client(ssh):
    try:
        return ssh.open_sftp()
    except Exception as e:
        logging.error("Getting the SFTP Client Error - {}".format(e))


def close_connection(ssh, sftp_client):
    try:
        sftp_client.close()
        ssh.close()
    except Exception as e:
        logging.error("Connection Closing Error - {}".format(e))


def get_latest_file(remote_file_path, sftp_client):
    try:
        latest = 0
        latestfile = None
        sftp_client.chdir(remote_file_path)
        for fileattr in sftp_client.listdir_attr():
            if fileattr.st_mtime > latest:
                latest = fileattr.st_mtime
                latestfile = fileattr.filename
        print(datetime.fromtimestamp(latest))
        return latestfile
    except Exception as e:
        logging.error("Getting the latest file name from server Error - {}".format(e))
        pass


def download_file(ssh, sftp_client, local_file_path, remote_file_path):
    try:
        latest_file_name = get_latest_file(remote_file_path, sftp_client)
        local_file_path = r"{}/{}".format(local_file_path, latest_file_name)
        sftp_client.get(
            r"{}/{}".format(remote_file_path, latest_file_name), local_file_path
        )
        close_connection(ssh, sftp_client)
        return local_file_path
    except Exception as e:
        logging.error("Downloading the latest file from server Error - {}".format(e))


def transfer_file(remote_file_path, local_file_path):
    try:
        ssh = establish_connection_local()
        sftp_client = get_sftp_client(ssh)
        sftp_client.put(
            r"{}".format(local_file_path),
            r"{}".format(remote_file_path),
        )
        close_connection(ssh, sftp_client)
    except Exception as e:
        logging.error("Transfer file to server Error - {}".format(e))


# ssh = establish_connection_local()
# sftp_client = get_sftp_client(ssh)
# print((sftp_client.listdir("/folder")))
# print(dir(sftp_client))
