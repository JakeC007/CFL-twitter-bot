"""
Written by Jake April 2, 2020
This script does a quick and dirty job of taking a clean input of words--one word/phrase 
per line-- and creating a string that is compatible with the Tracery JSON format.
format of RHS: ["word1", "word2", "word3"]
"""
def main():
  inputF = ''
  raw_inputF = input("Enter your .txt filename: ")
  inputF = raw_inputF + '.txt' 
  
  #Set up strings with the open bracket
  outputLST = "["

  #open file with word lists
  f = open(inputF, "r")

  #loop through the files, adding the nesscary accoutrements for formatting
  for line in f:
    reformat = "\"" + line.strip('\n') + "\", "
    outputLST+= reformat

  #Hacky way to get the close bracket on
  index = len(outputLST)-2
  
  #print desired output and copy from terminal
  print(outputLST[0:index] + "]\n")

main()
