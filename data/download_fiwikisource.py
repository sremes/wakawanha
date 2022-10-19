from argparse import ArgumentParser
from pathlib import Path
import requests
import subprocess


FIWIKISOURCE_DUMP_URL = "https://dumps.wikimedia.org/fiwikisource/20221001/fiwikisource-20221001-pages-articles-multistream.xml.bz2"
FIWIKISOURCE_DUMP_PATH = Path("fiwikisource.xml.bz2")


def download_to_file(url: str, filename: Path) -> None:
    if filename.exists():
        print(f"{filename} already exists, skipping download.")
        return
    print(f"Downloading {url} ...")
    r = requests.get(url, stream=True)
    with open(filename, "wb") as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)


def main():
    download_to_file(FIWIKISOURCE_DUMP_URL, FIWIKISOURCE_DUMP_PATH)
    subprocess.run(f"wikiextractor --json {FIWIKISOURCE_DUMP_PATH}", shell=True)


if __name__ == "__main__":
    main()
