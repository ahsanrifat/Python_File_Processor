import os
import SFTPFileExchange as sftp
import logging

logging.basicConfig(
    filename="file.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s - %(level)",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_file_from_server(
    hostname, username, password, port, server_directory, parent_directory
):
    ssh = sftp.establish_connection(hostname, username, password, port)
    sftp_client = sftp.get_sftp_client(ssh)
    local_file_path = sftp.download_file(
        ssh, sftp_client, parent_directory, server_directory
    )
    return local_file_path


def process_file(parent_directory, success_directory, error_directory):
    pass


def is_directory(path):
    return os.path.exists(path)


def on_process_success(file):
    # save file to success directory
    # remove file from parent directory
    pass


def on_process_error(file):
    # save file to error directory
    # remove file from parent directory
    pass
