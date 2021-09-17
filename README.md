# Python_practice_code
Practicing python language codes
#Read mode
# read_file=open('myself.txt','r')
# print(read_file.read())
#Write mode
# write_in_file=open('myself.txt','w')
# write_in_file.write('Riaz')
# write_in_file.close()
# f = open('myself.txt','r+')
# data = f.read()
# print(data.upper())
# print(data.lower())
# print(data[2])
# f.close()
# f = open('myself.txt','r+')
# a = f.read(1)
# f.close()
# print(a)
# appeand_file=open('myself.txt','a')
# appeand_file.write('\nSaman')
# appeand_file=open('myself.txt','r')
# print(appeand_file.read())
# print(appeand_file.tell())
# print(appeand_file.seek(40))
#Make object with 
# with open('myself.txt','r') as with_keyWard:
#     print(with_keyWard.read())
#read and write both
# raed_write_file=open('myself.txt','a+')
# raed_write_file.write('alia')
# read_file.close()
# print(raed_write_file.readable())
# print(raed_write_file.read())#problem(not read values)
#Next solution of this problem
# f = open('myself.txt','a+')
# f.write('\nali')
# f.close()
# f = open('myself.txt','r')
# a = f.read()
# f.close()
# print(a)
#Functions use
# print(raed_write_file.name)
# print(raed_write_file.closed)
# print(raed_write_file.mode)
# print(raed_write_file)
#Write a Python program to read an entire text file
# open_file=open('saman.txt','r')
# print(open_file.read())
# open_file=open('saman.txt','r')
# print(open_file.readlines())
# open_file=open('saman.txt','a')
# open_file.write('Zunaira')
# open_file=open('saman.txt','r')
# print(open_file.read())
#Write a Python program to read last n lines of a file.
# open_file=open('saman.txt','r')
# print(open_file.readlines()[-1])
#Write a Python program to read a file line by line and store it into a list.
# open_file=open('saman.txt','r')
# readfile=(open_file.readlines())
# l=list(open_file.readlines())
# print(l)
# for item in readfile:
#     print(item)
#     l.append(item)
# print(l)
# r=open_file.readline()
# print(r)
#Write a python program to find the longest words
# open_file=open('saman.txt','r')
# readfile=(open_file.readlines())
# max_num=max(readfile)
# print(max_num)
# less=0
# for item in readfile:
#     a=(len(item))
#     if a>less:
#         less=a
# print(less)
# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     # max_len = len(max(words, key=len))#Not understand
#     return [word for word in words if len(word) == max_len]

# print(longest_word('saman.txt'))
#Write a Python program to count the number of lines in a text file.
open_file=open('saman.txt','r')
readfile=(open_file.readlines())


    

    








