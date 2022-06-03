import time

class FiboIter():

    def __iter__(self): #Downder iter por el doble guion bajo
        self.n1 = 0
        self.n2 = 1
        self.counter = 0 
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2 || Se Remplaza con el swap
            #self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux #este es un swapping para invertir valores
            self.counter += 1 
            return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)

# 0 1 1
