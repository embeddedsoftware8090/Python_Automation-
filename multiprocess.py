import multiprocessing
x =open("data.txt","a")
print("The number of CPU currently working in system : ", multiprocessing.cpu_count())

print(multiprocessing.Process())
print(multiprocessing.Pipe())

print("The number of CPU currently working in system : ", multiprocessing.cpu_count(),file=x)

#print(multiprocessing.Process(),file=x)
#print(multiprocessing.Pipe(),file=x)

