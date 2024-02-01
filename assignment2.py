import urllib
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help='url to download')
    args = parser.parse_args()
    url = args.url

    def downloadData():
        with urllib.request.urlopen(url) as response:
            response = response.read().decode('utf-8')

        return response

    def processData():
        pass

