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

a = [10,88,23,49,30,76,100,35]
mergesort(a)