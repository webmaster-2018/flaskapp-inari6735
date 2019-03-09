#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stworz_baze.py
#
import os

from modele import *

from uczniowie.modele import baza, Klasa, Uczen, baza_plik


def main():
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen])
    baza.commit()
    baza.close()
    return 0

if __name__ == '__main__':
   import sys
   sys.exit(main())
