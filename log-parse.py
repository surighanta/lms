#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:04:15 2020

@author: suresh ganta
"""
import sys
import os
import csv
import re

class ParseLog:

    def readConf(self):
    #load conf file into class variables
        with open(self.cnfpath) as cnf_file:
            reader_tmp = csv.reader(cnf_file, delimiter=',')
            self.cmd_list = list(reader_tmp)

    def parseLog(self, file):
        #here open the log file and read for teh data
        print("Parsing the log file: %s/%s" %(self.logdir,file))
        fileFullPath= os.path.join(self.logdir, file)
        self.detailtdict = {}
        for i, line in open(fileFullPath):
            self.detailtdict[i] = line
            #print(line)
            

        """lines = 0
        for row in self.cmd_list:
            if lines == 0:
               print(f'Column names are {", ".join(row)}')
            else:
                print(f'\t{row[0]} -- {row[1]} -- {row[2]}  -- {row[3]} ')
            lines += 1
        print(f'Processed {lines} lines.')"""

    def readFiles(self, logdir):
    #read each file in directory
        print('Reading the conf file...')
        
        file_list = os.listdir(logdir)
        for file in file_list:
            self.parseLog(file)
        
    def __init__(self, logdir = ".", cnfpath = "seperators.conf"):
        print("Started parsing the log files...")
        print("Working dir: " + logdir)
        print("Using conf: " + cnfpath)
        self.logdir = logdir
        self.cnfpath = cnfpath

def main():
    parser = ParseLog(sys.argv[1], sys.argv[2])
    parser.readConf()
    parser.readFiles(parser.logdir)
    #ParseLog().run(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()