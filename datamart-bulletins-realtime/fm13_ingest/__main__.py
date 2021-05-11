
from fm13_ingest.decode_fm13 import decode
from fm13_ingest.ingest_to_db import DBIngester
import json
import click


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--level', default='decode', type=click.Choice(['decode', 'ingest'], case_sensitive=False))
def main(filename, level):
    if level == 'ingest':
        DBIngester().ingest(filename, metadata={})
        return

    with open(filename) as f:
        text = f.read()
    res = decode(text)
    print(json.dumps(res, indent=4))


if __name__ == '__main__':
    main()
