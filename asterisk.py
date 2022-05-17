def makeFrame (str):
  list = str.split()

  letterlist = [] #list for the length of each word
  for i in list:
    letterlist.append(len(i))
  
  longestWord = max(letterlist) #number for the longest word

  line = '*' * (longestWord + 4) #asterisk line for to and bottom
  print(line)

  for value in list:
    print('* ' + value + (' ' * (longestWord - len(value))) + ' *')

  print(line)

makeFrame('Python is a general-purpose language')
makeFrame('Learning a new programming language is a long process.')
makeFrame('Python can be used on a server to create web applications.')


