""" Quick sort berdasar kepada pendekatan divide-and-conquer dengan memilih satu elemen sebagai elemen pivot dan mempartisi array sehingga; sisi kiri pivot memiliki semua elemen dengan nilai yang lebih kecil dibandingkan elemen pivot, dan sisi kanan memiliki semua elemen dengan nilai yang lebih besar dibandingkan nilai elemen pivot.

Adapun langkah programnya sebagai berikut :

     Misalnya Kita mempunyai data A yang mempunyai N elemen. Kita pilih sembarang elemen dari data tersebut, biasanya elemen pertama, kita misalkan x.
    Kemudian semua elemen tersebut disusun dengan menempatkan X pada posisi J sedemikian rupa sehingga elemen ke 1 sampai pada J-1 mempunyai nilai lebih besar dari X
    Hingga seterusnya diulang setiap sub data.
 """

def quicksort(a, mulai, akhir) :
    if mulai < akhir :
        pyindex = partisi(a, mulai, akhir)
        quicksort(a, mulai, pyindex-1)
        quicksort(a, pyindex+1, akhir)

def partisi(a, mulai, akhir) :
    middle = int(akhir/2)
    pivot = a[middle]
    pyindex = mulai
    for i in range(mulai, middle) :
        if a[i]>=pivot :
            a[i], a[pyindex] = a[pyindex], a[i]
            pyindex = pyindex+1
    a[pyindex], a[middle] = a[middle], a[pyindex]
    print(a)
    return pyindex

a = [68, 99, 70, 34, 47, 2, 14, 86, 24]
quicksort(a,0,len(a)-1)