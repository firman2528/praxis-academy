""" Insertion sort adalah sebuah metode pengurutan data dengan menempatkan setiap elemen data pada pisisinya dengan cara melakukan perbandingan dengan data – data yang ada.

 Adapun langkah programnya sebagai berikut :

    Bandingkan data ke-2 dengan data ke-1 ,jika data ke-2 lebih kecil maka tukar posisinya, jika tidak maka biarkan saja.
    Bandingkan data ke-3 dengan data ke-2 dan data ke-1 ,jika data ke-3 lebih kecil maka tukar lagi posisinya.
    Bandingkan data ke-4 dengan data ke-3 ,data ke-2 dan data ke-1 , jika data ke-4 lebih kecil dari ketiganya maka tukar dan pindahkan data ke-4 ke paling depan. Begitu seterusnya hingga data terurut.
 """


def insertsort(a) :
    for i in range(len(a)-1,-1,-1) :
        value = a[i]
        hole = i
        while hole<(len(a)-1) and a[hole+1] > a[hole] :
            a[hole] = a[hole+1] 
            hole = hole + 1
            a[hole] = value
        print(a)
# a = [35, 3, 40, 55, 12, 8, 79, 64]
# insertsort(a)


""" Merge Sort adalah salah satu sorting dengan metode memecah data kemudian
menyelesaikannya setiap bagian dan menggabungkannya kembali hingga data terurut.

Adapun langkah programnya sebagai berikut :

    Pertama data dipecah menjadi 2 bagian dimana bagian pertama merupakan setengah (jika data genap) atau setengah minus satu (jika data ganjil) dari seluruh data, kemudian dilakukan pemecahan kembali untuk masing-masing blok sampai hanya ada satu data dalam satu blok.
    Setelah digabungkan kembali dengan membandingkan pada blok yang sama apakah data pertama lebih besar dari pada data ke-tengah+1 , jika iya maka data ke-tengah+1 dipindah menjadi data pertama. Kemudian data pertama tadi sampai data ke-tengah dipindah menjadi data ke-dua sampai data ke-tengah+1.
    Begitu seterusnya hingga membentuk data yg terurut dalam satu blok yang utuh seperti awalnya. Sehingga merge sort membutuhkan fungsi rekursif dalam penyelesainnya """

def mergesort(a):
    print('memecah',a)
    n=len(a)
    if n<2:
        return a
    else:
        mid=n//2
        left=a[:mid]
        right=a[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i< len(left) and j<len(right):
            if left[i]>right[j]:
                a[k]=left[i]
                i=i+1
            else:
                a[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            a[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            a[k]=right[j]
            j=j+1
            k=k+1
    print('menggabungkan',a)

# a = [10,88,23,49,30,76,100,35]
# mergesort(a)



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

# a = [68, 99, 70, 34, 47, 2, 14, 86, 24]
# quicksort(a,0,len(a)-1)


""" Selection Sort adalah sorting dengan prinsip memilih elemen dengan nilai paling rendah dan menukar elemen tersebut dengan elemen ke-i. Nilai dari i dimulai dari 1 ke n, dimana n adalah julah total elemen dikurangi 1.

 Adapun langkah programnya sebagai berikut :

     Pengecekan dimulai dari data ke-1 sampai data ke-n.
    Tentukan bilangan dengan index terkecil dari data bilangan tersebut.
    Tukar bilangan index terkecil tersebut dengan bilangan pertama (i= 1).
    Ulangi langkah 2 dan 3 dengan bilangan index (i= i+1) hingga data terurut semuanya
 """

def seleksi(pylis) :
    pengulangan = 0
    for i in range(len(pylis)-1) :
        minim = i
        for j in range(i+1, len(pylis)) :
            if pylis[j] < pylis[minim] :
                minim = j
        pengulangan +=1
        pylis[minim], pylis[i] = pylis[i], pylis[minim]
        print(pengulangan, pylis)

# pylis= [54,26,93,17,77,31,44,55,20,21,34,65,70,88,100,49]
# seleksi(pylis)


""" Bubble sort (metode gelembung) adalah metode/algoritma pengurutan dengan dengan cara melakukan penukaran data dengan tepat disebelahnya secara terus menerus sampai bisa dipastikan dalam satu iterasi tertentu tidak ada lagi perubahan. Jika tidak ada perubahan berarti data sudah terurut. Disebut pengurutan gelembung karena masing-masing kunci akan dengan lambat menggelembung ke posisinya yang tepat.
Algoritma ini termasuk dalam golongan algoritma comparison sort, karena menggunakan perbandingan dalam operasi antar elemennya. Berikut ini adalah gambaran dari algoritma bubble sort:

    Bandingkan nilai data ke-1 dan data ke-2
    Jika data ke-1 lebih besar dari data ke-2 maka tukar posisinya
    Kemudian data yg lebih besar tadi dibandingkan dengan data ke-3
    Lakukan langkah nomer 2 hingga selesai
 """

def bubblesort(pylist) :
    n = 0
    for m in range(len(pylist)-1) : #model biasa
        for l in range(len(pylist)-1-m) :
            if pylist[l]>pylist[l+1] :
                pylist[l], pylist[l+1] = pylist[l+1], pylist[l]

        n+=1
        print(n, pylist)

# pylist = [32,3,15,4,33,18,5,34]
# bubblesort(pylist)
    