# All python imports
from os import path

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
  c = SyllableCounter()
  c.count(INPUT_DIRECTORY, OUTPUT_DIRECTORY)

if __name__ == '__main__':
  main()
