from urllib.request import urlopen


def get_local_file_content(file_path: str) -> str:
    """Gets the contents of a local file.

    Args:
        file_path: The path of the file.

    Returns:
        The content fetched from the local file.
    """
    with open(file_path, "r") as opened_file:
        content: str = opened_file.read()
        return content


def get_remote_file_content(url: str) -> str:
    """Gets the contents of a remote file.

    Args:
        url: The url of the file.

    Returns:
        The content fetched from remote file.
    """
    with urlopen(url) as loaded_file:
        content: str = loaded_file.read().decode("utf-8")
        return content
