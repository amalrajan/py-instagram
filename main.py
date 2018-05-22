import argparse
import bs4 as bs
import urllib.request
import sys
import os
import datetime


def argument_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('type', type=str, help="single / multiple")
    parser.add_argument('url', type=str, help="url / path to text file")
    parser.add_argument('-o', '--output', type=str,
                        default=os.getcwd(), help="output destination")

    args = parser.parse_args()
    main(args)


def download_image(url, dest):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    image = soup.find('meta', property='og:iamge')['content']
    title = str(datetime.datetime.now().replace(':', '-'))
    path = "{}\{}.jpg".format(dest, title)


def download_image(url, dest):
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    image = soup.find("meta", property="og:image")["content"]
    title = str(datetime.datetime.now()).replace(':', '-')
    path = "{}\{}.jpg".format(dest, title)

    with open(path, 'wb') as file:
        file.write(urllib.request.urlopen(image).read())


def main(args):
    if args.type == "single":
        download_image(args.url, args.output)
    elif args.type == "multiple":
        with open(args.url) as batch_file:
            urls = batch_file.read().split('\n')
        for url in urls:
            download_image(url, args.output)


if __name__ == "__main__":
    argument_parser()
