import find_prime_number
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())


def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = ext_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, gcd

def mod_inverse(e, n):
    # inverse of e mod n
    x, y, gcd = ext_gcd(n, e)
    y += n
    return y

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def generate_key_list(keys, prime_n):
    big_list = []
    for i in range(keys + 1):
        # random 617 digit
        big_list.append(find_prime_number.generate_large_prime(prime_n))
    return big_list

def plt_and_save_img(list1, list2, save_img = False):
    plt.plot(list1, label='RSA decrypt time', color='blue')
    plt.plot(list2, label='CRT_RSA decrypt time', color='green')
    plt.title('Compare Decrypt Time')
    plt.xlabel('message')
    plt.ylabel('time')
    plt.legend()
    plt.show()

    if save_img == True:
        plt.savefig('./myplot.png')

