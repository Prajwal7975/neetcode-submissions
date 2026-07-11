class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr=[None]*capacity
        self.size=0
        self.capacity=capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size]=n
        self.size+=1    

    def popback(self) -> int:
        value=self.arr[self.size-1]
        self.arr[self.size-1]=None
        self.size-=1
        return value
 

    def resize(self) -> None:
        for i in range (len(self.arr)):
            self.arr.append(None)
        self.capacity= len(self.arr)   


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
