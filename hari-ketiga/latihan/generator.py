class Generator :
    def reverse(data) :
        for index in range(len(data) -1, -1, -1) :
            yield data[index]


    def iterator() :
        for char in reverse('golf') :
            print(char)