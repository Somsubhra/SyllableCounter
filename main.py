# All python imports
from os import walk, path, stat, mkdir

# All constant definitions
INPUT_DIRECTORY = 'corpus'
OUTPUT_DIRECTORY = 'out'

# The syllable counter class
class SyllableCounter:

  # Count the number of syllables
  def count(self, inputFile, outputFile):
    print inputFile
    print outputFile


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
      c.count(inputFile, path.join(OUTPUT_DIRECTORY, dirPath, fileName))

if __name__ == '__main__':
  main()
