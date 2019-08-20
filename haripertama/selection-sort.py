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

pylis= [54,26,93,17,77,31,44,55,20,21,34,65,70,88,100,49]
seleksi(pylis)