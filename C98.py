def countWordsFromFile():
    wordCount = 0
    fileName = input("ENTER YOUR FILE NAME HERE :-")
    file = open(fileName, 'r')
    
    for i in file:
        splitData = i.split()
        wordCount = wordCount+len(splitData)
        print(splitData)
        print(len(splitData))
        print(wordCount)
countWordsFromFile()

