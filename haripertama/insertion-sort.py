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
a = [35, 3, 40, 55, 12, 8, 79, 64]
insertsort(a)