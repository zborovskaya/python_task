from multiprocessing import Pool
from  datetime import datetime
def if_prime(a):
     print(a[0])
     print(a[1])
def prok():
     a = [[i, "bgrbh"] for i in range(10)]
     if __name__ == '__main__':
          with Pool(8) as p:
               # p.map(if_prime, a )
               p.imap_unordered(if_prime, a )

start = datetime.now()
prok()
# print(list(range(10),'rrr'))
end = datetime.now()
# a=[(i,"bgrbh") for i in range(10)]
# print(a)
print("Время работы " + str(end-start)+ '\n')
print("my change")



