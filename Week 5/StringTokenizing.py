def tokenezier(inputString,delimiter):
    tokens=inputString.split(delimiter)
    for i in tokens:
        print(i,end=" ")



messageString="Greetings! I|am|a|GC|IS 123 Student"
delimiter="|"
tokenezier(messageString,delimiter)