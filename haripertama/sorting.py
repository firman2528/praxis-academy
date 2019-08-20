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

pylist = [32,3,15,4,33,18,5,34]
bubblesort(pylist)
    