"""
Written by Jake April 2, 2020
This script does a quick and dirty job of taking a clean input of words--one word/phrase 
per line-- and creating a string that is compatible with the Tracery JSON format.
format of RHS: ["word1", "word2", "word3"]
"""

def main():
  #Set up strings with the open bracket
  outputN = "["
  outputV = "["
  outputAdv = "["

  #open files with word lists
  fN = open("inputN.txt", "r")
  fV = open("inputV.txt", "r")
  fAdv = open("inputAdv.txt", "r")

  #loop through the files, adding the nesscary accoutrements for formatting
  for line in fN:
    reformat = "\"" + line.strip('\n') + "\", "
    outputN+= reformat

  for line in fV:
    reformat = "\"" + line.strip('\n') + "\", "
    outputV+= reformat

  for line in fAdv:
    reformat = "\"" + line.strip('\n') + "\", "
    outputAdv+= reformat

  #Hacky way to get the close bracket on
  indexN = len(outputN)-2
  indexV = len(outputV)-2
  indexAdv = len(outputAdv)-2
  
  #print desired output and copy from terminal
  print(outputN[0:indexN] + "]\n")
  print(outputV[0:indexV] + "]\n")
  print(outputAdv[0:indexAdv] + "]\n")
