log=open('log.txt', 'w')
print (1,2,3, file=log)
log.close()
print (1,2,3)
