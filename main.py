#!/usr/bin/env python

"""main.py: Counts number of syllables in words"""

__author__ = "Somsubhra Bairi"
__copyright__ = "Copyright 2014, Somsubhra Bairi"
__license__ = "Apache License, Version 2.0"
__email__ = "somsubhra.bairi@gmail.com"

# All python imports
from os import walk, path, stat, mkdir, makedirs

# All constant definitions
INPUT_DIRECTORY = 'corpus'
OUTPUT_DIRECTORY = 'out'

# The syllable counter class
class SyllableCounter:

  # Count the number of syllables
  def count(self, inputFileName, outputFileName):
    inputFile = open(inputFileName)
    content = inputFile.read()

    outputFile = open(outputFileName, 'w+')
    outputFile.write(content)

    inputFile.close()
    outputFile.close()

# The main method
def main():

  # Check for the input directory
  try:
    stat(INPUT_DIRECTORY)
  except:
    print "No files present in input directory " + INPUT_DIRECTORY + "..."
    print "Terminating program..."
    exit()

  # Create the output directory
  try:
    stat(OUTPUT_DIRECTORY)
  except:
    mkdir(OUTPUT_DIRECTORY)

  # Create instance of the syllable counter
  c = SyllableCounter()

  # Walk through the input directory and count number of syllables
  for(dirPath, _, fileNames) in walk(INPUT_DIRECTORY):
    for fileName in fileNames:
      inputFile = path.join(dirPath, fileName)

      outputFile = path.join(OUTPUT_DIRECTORY, dirPath, fileName)
      outputDir = path.join(OUTPUT_DIRECTORY, dirPath)

      try:
        stat(outputDir)
      except:
        makedirs(outputDir)

      c.count(inputFile, outputFile)

if __name__ == '__main__':
  main()
