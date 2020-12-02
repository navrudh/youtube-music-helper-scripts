from ytmusicapi import YTMusic


def get_client(auth=True, auth_file='env/headers_auth.json'):
    if not auth:
        return YTMusic()

    return YTMusic(auth_file)
