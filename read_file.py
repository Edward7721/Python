# Open a file, read line by line, print the number of lines, print the number of words.

def countlines(filepath):
    count =0
    with  open(filepath)as f:
         for line in f:
            count= count +1
    return count

def countwords(filepath):
    count =0
    with  open(filepath)as f:
          for line in f:
              count +=  len(line.split())
    return count



print (countlines("c://temp/file.txt"))
print (countwords("c://temp/file.txt"))
