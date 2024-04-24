vocab_words = {"mundane":"commonplace and often boring", "retrogress":"to return to an earlier and usually worse condition; to move or travel backward", "incipient":"beginning to appear or develop", "perfidy":"treachery or deceit", "covert":"not intended to be seen, known, or found out", "descry":"to catch sight of something", "transitory":"not permanent or lasting, but existing only for a short time", "hoax":"an act intended to trick people into believing something is real when it is not", "penury":"extreme poverty", "stigma":"the shame or disgrace attached to something regarded as socially unacceptable"}

def define(dict, s, msg1, msg2):

  g = "yes"
  
  while g == "yes":
    keyword = input(s)
    if dict.get(keyword, 0) != 0:
      print(msg1, keyword, msg2, dict[keyword] + ".")
      g = input("Search again? yes/no ")
    else:
      print("ERROR")

define(vocab_words, "What word are you looking for?", "The word", "means")