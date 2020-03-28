#!/usr/bin/env python

import csv
import database

def extract(csvfile,db):
    with open(csvfile) as f:
        c = csv.reader(f)
        firstrow=True
        for row in c:
            #print(row[1:])
            if firstrow:
                firstrow=False
                continue
            db.insertExample(row[1:])

if __name__ == '__main__':
    db=database.Database()
    if input("Reset Database? Y/N: ")=="Y":
        db.reset()
    if input("Insert examples from CSV? Y/N: ")=="Y":
        csvfile = input("CSV filename: ")
        extract(csvfile,db)
