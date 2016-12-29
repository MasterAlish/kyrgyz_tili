# coding=utf-8
import sys

from kg.db.generate_words import generate

try:
    if len(sys.argv) > 1:
        generate(sys.argv[1])
    else:
        generate()
except Exception as e:
    print(u"Ката:")
    print("\t"+e.message)