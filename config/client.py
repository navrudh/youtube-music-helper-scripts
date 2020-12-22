from ytmusicapi import YTMusic


def get_client(auth=True, auth_file='../env/headers_auth.json'):
    if not auth:
        return YTMusic()

    # print(Path(auth_file).read_text())

    return YTMusic(auth_file)
