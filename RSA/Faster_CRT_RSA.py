import time
import library


def Faster_CRT_RSA_time(p, q, e):
    # check p & q
    if library.gcd(p - 1, q - 1) == 2:
        # key generate
        n = p * q
        d = library.mod_inverse(e, (p - 1) * (q - 1))
        print(d)
        dp = (d - 1) // 2 % ((p - 1) // 2)
        dq = (d - 1) // 2 % ((q - 1) // 2)
        N = (p - 1) * (q - 1) // 4
        N1 = (q - 1) // 2
        N2 = (p - 1) // 2
        N1_inv = library.mod_inverse(N1, N2) % N2
        N2_inv = library.mod_inverse(N2, N1) % N1
        d_prime = (dp * N1 * N1_inv + dq * N2 * N2_inv) % N
        print(d_prime)
        M1 = library.mod_inverse(q, p)
        M2 = library.mod_inverse(p, q)

        print("RSA public key <n, e>:<%d, %d>" % (n, e))
        print("RSA private key <p, q, dp, dq>：<%d, %d, %d, %d>" % (p, q, dp, dq))

        decrypt_time = []
        total_time_start = time.time()

        for m in range(100):
            # encrypt
            c = pow(m, e, n)

            # decrypt
            decrypt_time_start = time.time()
            a1 = pow(c, dp, p)
            print(a1)
            a2 = pow(c, dq, q)
            print(a2)
            de_m = (a1 * q * M1 + a2 * p * M2) % n
            decrypt_time_end = time.time()
            print("Decrypt time: %.15f" % (decrypt_time_end - decrypt_time_start))
            decrypt_time.append(decrypt_time_end - decrypt_time_start)

            if m != de_m:
                print("ERROR! message: %d, decrypt message: %d" % (m, de_m))

        total_time_end = time.time()
        total_time = total_time_end - total_time_start
        print("Total time = ", total_time)

        return decrypt_time, total_time
    else:
        print("gcd((p-1), (q-1)) need to be 2")
        print(library.gcd(p-1, q-1))
        return -1



if __name__ == '__main__':
    # 617位數
    # big_list = [1523009694626829739047061473024592973786533537601347598556621693663948158651174349692336366662202659401671080898858772495083316029202896465632122492127235406769085575510158965494898497842637123920025244898914883813574987405773113784992794945160012329902959673394934803207139331067342002182153444971025370392833410263023059835999058994179085038138645992396179636451419975407393196508285074284116362282661039152516747871959547817200140951192520887707538230189229949389038768247360472049948024794896069641575789755566965610556181540489883482241499689651337431906523570405541484298725868471769056053923094221999573955333,
    #             15777721434851325715007823064836246627187405853158969518731094678160487646706027204151059918674288576879363253182613364991448760298181698312103775492791741714238421461526334659368906138109231350305552883811024110833916114937086805244783117861824386670290193185939582363038646689686123198569760127809267233120104541173774520785341466923218424979690372754367752779068669605182970588029226437364611060723247427003166372796493891131302367646467697670434635304171804557105344014951192936970264490339047635512063800321598439391012102616855787576433643758028201844387228916980285264014978262608118102378702841635639460843633,
    #             12635540328928605730746079018223767856159415051525859511052581769765632816494835984747270112386332040238647853588341205839277950151086610403985994420408907894021637477313149466767163750375913975551674674266150171887173637883183300981193400630796281179078385992710719769848753666802951099653027229503093106554346269088251853648016529293027529780602695047308647886047112973360319872873222674221317369267272480999499159287788351512231177846577850709127484295181606447796657157606114688816221506429281649872858781859597254506944273476480979059686363793633439932062500639498938144692814866480169601800953763378119173818703]

    # big_list = [find_prime_number.generate_large_prime(512),
    #             find_prime_number.generate_large_prime(512),
    #             find_prime_number.generate_large_prime(512)]

    big_list = [19, 17, 7]

    p, q, e = big_list  # can change this part
    print("gcd(e, (p-1)(q-1)) = ", library.gcd(e, (p-1)*(q-1)))

    Faster_CRT_RSA_time(p, q, e)