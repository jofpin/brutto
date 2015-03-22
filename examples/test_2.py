#!/usr/bin/env python
# -*- coding: utf-8 -*-

from brutto_easy import Brutto

main = Brutto()

for example in main.increase(scope=8, letters=True, numbers=True, symbols=False):
    print example
