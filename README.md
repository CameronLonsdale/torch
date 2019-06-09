# torch

Command-line Cryptanalysis

## Installation

Within a virtual environment:
```
pip3 install -U torch-crypto
```

Globally:
```
sudo pip3 install -U torch-crypto
```

## Usage

```shell
$ torch -h          
Usage: torch [OPTIONS] COMMAND [ARGS]...

  Command-line Cryptanalysis.

  Easily crack and decrypt classic ciphers from a terminal.

Options:
  -n INTEGER     The upper limit on the number of possible decryptions to be
                 printed
  -v, --verbose  Additionally print out the key and score for each decryption
  -h, --help     Show this message and exit.

Commands:
  shift         Decrypt or crack a shift cipher
  substitution  Decrypt or crack a simple substitution cipher
  vigenere      Decrypt or crack a vigenere cipher
```

### Example - Krypton Level 3

```shell
$ cat cipher  | torch -v substitution --ntrials 2
INCRY PTOGR APHYA CAESA RCIPH ERALS OKNOW NASAC AESAR SCIPH ERTHE SHIFT
CIPHE RCAES ARSCO DEORC AESAR SHIFT ISONE OFTHE SIMPL ESTAN DMOST WIDEL
YKNOW NENCR YPTIO NTECH NIQUE SITIS ATYPE OFSUB STITU TIONC IPHER INWHI
CHEAC HLETT ERINT HEPLA INTEX TISRE PLACE DBYAL ETTER SOMEF IXEDN UMBER
OFPOS ITION SDOWN THEAL PHABE TFORE XAMPL EWITH ASHIF TOFAW OULDB EREPL
key: QAZWSXEDCRFVTGBYHNUJMIKOLP
score: -9194.23851696

$ torch substitution -k QAZWSXEDCRFVTGBYHNUJMIKOLP
KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
WELLD ONETH ELEVE LFOUR PASSW ORDIS BRUTE
```
### Torch versus Krypton

[OverTheWire Krypton Wargame](http://overthewire.org/wargames/krypton/)

[![asciicast](https://asciinema.org/a/5J1NTPowvpPjyaKuoQkmLF4aB.png)](https://asciinema.org/a/5J1NTPowvpPjyaKuoQkmLF4aB)
