def define(dict, s, msg1, msg2):

  g = "yes"
  
  while g == "yes":
    word = input(s)
    if dictionary.get(word, 0) != 0:
      print(msg1, word, msg2, dictionary[word] + ".")
      g = input("Search again? yes/no ")
    else:
      print("ERROR")
