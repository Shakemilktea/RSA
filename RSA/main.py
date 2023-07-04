import library, find_prime_number
import RSA, CRT_RSA
import argparse
import sys


if __name__ == '__main__':
    """
        cmd: python main.py --keys 3 --prime_n 1024
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--keys', type=int, default=2, help='input the number of key')  # key should not lower then 2
    parser.add_argument('--prime_n', type=int, default=1024, help='generate a large prime number of n bits')
    parser.add_argument('--iter', type=int, default=100, help='message iter times')
    args = parser.parse_args()
    print(args)

    if args.keys > 1:
        big_list = library.generate_key_list(args.keys, args.prime_n)
    else:
        print("KEY SHOULD NOT LOWER THEN 2")
        sys.exit()

    list1, time1 = RSA.RSA_time(big_list, args.iter)
    list2, time2 = CRT_RSA.CRT_RSA_time(big_list, args.iter)

    print("Speed up %.1f%%" % ((time1 - time2) / time1 * 100))
    library.plt_and_save_img(list1, list2)

