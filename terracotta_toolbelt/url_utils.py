import urllib.parse


# https://stackoverflow.com/questions/1793261/how-to-join-components-of-a-path-when-you-are-constructing-a-url-in-python
def urljoin(*pieces):
    return '/'.join(s.strip('/') for s in pieces)


def singleband_url(api_url, *keys, **kwargs):
    url = urljoin(api_url, "singleband", *keys, "{z}/{x}/{y}.png")
    return f"{url}?{urllib.parse.urlencode(kwargs)}"


def point_url(api_url, lat, lon, *keys):
    return urljoin(api_url, "point", *keys, "{:.4f}/{:.4f}".format(lat, lon))
