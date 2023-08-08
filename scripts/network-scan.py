import requests
import ipaddress
import json
from bs4 import BeautifulSoup


class site_host:
    def __init__(self, url, title):
        self.url = url
        self.title = title


def main():

    network = ipaddress.IPv4Network(u'192.168.50.51/24', strict=False)
    hosts = network.hosts()
    found_hosts = list()
    for ip in hosts:
        # A GET request to the API
        try:
            url = f"http://{ip}"
            response = requests.get(url, timeout=0.1)

            soup = BeautifulSoup(response.text, 'html.parser')
            host_title = ""
            for title in soup.find_all("title"):
                host_title += title.get_text()

        # Print the response
            print(f"{ip}: {response.status_code} {host_title}")
            found_hosts.append(site_host(url, host_title))
        except:
            print(f"{ip}: No response on port 80")
    print(f"{len(found_hosts)} hosts responded on network")
    host_properties = list()

    for host in found_hosts:
        host_properties.append({"url": host.url, "title": host.title})

    host_json = json.dumps(host_properties)
    with open('sites.json', 'w') as outfile:
        json.dump(host_json, outfile)


main()
