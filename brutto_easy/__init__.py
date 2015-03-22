#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2015 Jose Pino, @jofpin  <jofpin@gmail.com>
#
#######################################
import itertools                      #
from itertools import chain, product  #
from random import sample             # 
try:                                  #
    from string import (              #
        digits as numb,               #
        letters as lett,              #
        whitespace as spac,           #
        punctuation as symb,          #
    )                                 ###############################
except:                                                             #
    print "\t\nError: Something bad has happened in the import!\n"  #
                                                                    #
#####################################################################
#
# Brutto
#
#############################################################
# Generate characters for gross , very easy strength.       #
#############################################################
#    These are the options , which must customize.          #         
#    letters:> add letters  by default is True.             #
#    numbers:> add numbers. by default is True.             #
#    symbols:> add symbols  by default is False.            #
#    scope:>  add scope. customize value                    #
#############################################################

class Brutto:

    def increase(self, letters=True, numbers=True, symbols=False, space=False, scope=4):
        # Seting of imports
        rang = 1
        char = ""
        char += spac if space else char
        char += lett if letters else char
        char += numb if numbers else char
        char += symb if symbols else char
        char = "".join(sample(char, len(char)))

        # Return relations
        return ("".join(conex) for conex in chain.from_iterable(product(char, repeat = value,) for value in range(rang, scope + rang),))

    def direct(self, value):
        char = ""
        char += lett
        char += numb
        char += symb
        # def play
        for path in itertools.imap("".join, itertools.product(char, repeat = value)):
            print path