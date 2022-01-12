from urllib.request import urlopen


def get_local_file_content(file_path):
    """Gets the contents of a local file.

    Args:
        file_path: The path of the file.

    Returns:
        The content fetched from the local file.
    """
    with open(file_path, "r") as opened_file:
        return opened_file.read()


def get_remote_file_content(url):
    """Gets the contents of a remote file.

    Args:
        url: The url of the file.

    Returns:
        The content fetched from remote file.
    """
    with urlopen(url) as loaded_file:
        return loaded_file.read().decode("utf-8")
