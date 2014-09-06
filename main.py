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


##########################################
## The Gujarati Universal Character set ##
##########################################
class GujaratiUTF:

  # Declaration of language specific lists
  separators = [u".", u"!", u"?"]
  breakers = [u",", u";", u":"]

  halan = u'\u0acd'

  # Signs
  m_chandrabindu = u'\u0a81'
  m_anusvar = u'\u0a82'
  m_visarga = u'\u0a83'
  m_nukta = u'\u0abc'
  m_avagraha = u'\u0abd'

  # Independent vowels
  l_a = u'\u0a85'
  l_aa = u'\u0a86'
  l_i = u'\u0a87'
  l_ii = u'\u0a88'
  l_u = u'\u0a89'
  l_uu = u'\u0a8a'
  l_v_r = u'\u0a8b'
  l_v_l = u'\u0a8c'
  l_ae = u'\u0a8d'
  l_e = u'\u0a8f'
  l_ai = u'\u0a90'
  l_au = u'\u0a91'
  l_o = u'\u0a93'
  l_ow = u'\u0a94'

  # Consonant
  l_ka = u'\u0a95'
  l_kha = u'\u0a96'
  l_ga = u'\u0a97'
  l_gha = u'\u0a98'
  l_nga = u'\u0a99'
  l_ca = u'\u0a9a'
  l_cha = u'\u0a9b'
  l_ja = u'\u0a9c'
  l_jha = u'\u0a9d'
  l_nya = u'\u0a9e'
  l_tta = u'\u0a9f'
  l_ttha = u'\u0aa0'
  l_dda = u'\u0aa1'
  l_ddha = u'\u0aa2'
  l_nna = u'\u0aa3'
  l_ta = u'\u0aa4'
  l_tha = u'\u0aa5'
  l_da = u'\u0aa6'
  l_dha = u'\u0aa7'
  l_na = u'\u0aa8'
  l_pa = u'\u0aaa'
  l_pha = u'\u0aab'
  l_ba = u'\u0aac'
  l_bha = u'\u0aad'
  l_ma = u'\u0aae'
  l_ya = u'\u0aaf'
  l_ra = u'\u0ab0'
  l_la = u'\u0ab2'
  l_lla = u'\u0ab3'
  l_va = u'\u0ab5'
  l_sha = u'\u0ab6'
  l_ssa = u'\u0ab7'
  l_sa = u'\u0ab8'
  l_ha = u'\u0ab9'

  # Dependent vowels
  m_aa = u'\u0abe'
  m_i = u'\u0abf'
  m_ii = u'\u0ac0'
  m_u = u'\u0ac1'
  m_uu = u'\u0ac2'
  m_v_r = u'\u0ac3'
  m_v_rr = u'\u0ac4'
  m_ae = u'\u0ac5'
  m_e = u'\u0ac7'
  m_ai = u'\u0ac8'
  m_au = u'\u0ac9'
  m_o = u'\u0acb'
  m_ow = u'\u0acc'

  l_om = u'\u0ad0'
  l_ru = u'\u0af1'
  l_ri = u'\u0ae0'
  l_lri = u'\u0ae1'

  # Digits
  l_0 = u'\u0ae6'
  l_1 = u'\u0ae7'
  l_2 = u'\u0ae8'
  l_3 = u'\u0ae9'
  l_4 = u'\u0aea'
  l_5 = u'\u0aeb'
  l_6 = u'\u0aec'
  l_7 = u'\u0aed'
  l_8 = u'\u0aee'
  l_9 = u'\u0aef'

  # Consonants ordered based on the tongue action backward to forward
  ordered_consonants = [l_ha, l_a, l_ka, l_ga, l_kha, l_gha, l_ca, l_ja, l_cha, l_sha, l_jha, l_ssa, l_nya,
                        l_ya, l_da, l_dha, l_tha, l_ta, l_na, l_la, l_ra, l_sa, l_tta, l_dda, l_ddha, l_ttha,
                        l_nna, l_lla, l_nga, l_pha, l_va, l_ma, l_bha, l_ba, l_pa]

##########################################
## End Gujarati Universal Character Set ##
##########################################


# The syllable counter class
class SyllableCounter:

  # Count the number of syllables
  def count(self, input_file_name, output_file_name):
    input_file = open(input_file_name)
    content = input_file.read()
    content = content.decode("utf-8")

    words = content.split()

    print "Parsing input file " + input_file_name + " containing " + str(len(words)) + " words..."

    output_file = open(output_file_name, 'w+')

    for word in words:
      output_file.write(word.encode("utf-8"))
      output_file.write("\n")

    input_file.close()
    output_file.close()


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
  for(dir_path, _, file_names) in walk(INPUT_DIRECTORY):
    for file_name in file_names:
      input_file = path.join(dir_path, file_name)

      output_file = path.join(OUTPUT_DIRECTORY, dir_path, file_name)
      output_dir = path.join(OUTPUT_DIRECTORY, dir_path)

      # Create the output directory path
      try:
        stat(output_dir)
      except:
        makedirs(output_dir)

      c.count(input_file, output_file)


if __name__ == '__main__':
  main()
