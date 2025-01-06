# Malphonetic
Find words that would make a poor example for the phonetic alphabet, by finding words whose initial sound is a homophone (or close to one) of another letter.

## Installation
There are no dependencies required, this will run with a modern Python 3 alone. It requires an export of the Wiktionary data file `enwiktionary-????????-pages-meta-current.xml.bz2` from https://dumps.wikimedia.org/backup-index-bydb.html

## Usage
Run with a single argument, pointing to the wiktionary data file, e.g.:

    python3 main.py ./enwiktionary-20241220-pages-meta-current.xml.bz2

It can also be run with an input path of `-`, which can be used in combination with `pv` to get an ETA.

    pv < ./enwiktionary-20241220-pages-meta-current.xml.bz2 | python3 main.py -

