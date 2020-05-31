free = int(input('Enter free bytes in disk'))
used = int(input("Enter used bytes in disk"))
delete_file = int(input("Enter bytes of deleted file"))
new_file = int(input('Enter the bytes of new file'))
free = free - used + delete_file - new_file
print(f'Free bytes in disk: {free}')



'''
A floppy disj shows 'f' bytes free and 'u' bytes used. If you delete a file of size 'o' bytes and create a new file of size 'o' bytes. how many bytes of free memory is in disk?

'''