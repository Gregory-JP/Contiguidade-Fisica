class Contiguity_list:
    def __init__(self, size):
        self.node = [0] * size
        self.begin = 0
        self.end = -1
        self.size = size 
    
    def show_list(self):
        aux = self.begin
        if (aux == - 1):
            print("Lista não existe")
        else:
            print(self.node)
    

    def locate_node(self, value):
        i = 0
        self.end = self.size   
        if(value <= self.end or value >= self.begin):
            for i in range(self.end):            
                if (value == self.node[i]):
                    return print("Valor procurado", value, ",encontrado na posição", i + 1)                       
        else:
            print("Valor não encontrado!")
           

    def insert_node(self, location, value):        
        if ((location > self.size - 1) or ((location < self.begin) and (location > self.end - 1))) :
            print ("Error: Posição não encontrada ou inválida")    
        else:
            if (self.begin == - 1):
                self.end = 0
                for i in range (self.begin, self.begin + location):
                    self.node[i - 1] = self.node[i]
                self.begin = self.begin - 1
            self.node[self.begin + location ] = value

    def remove_node(self, location):
        if ((location > self.size - 1) or ((location < self.begin) and (location > self.end - 1))) :
            print ("Posição não encontrada ou inválida")
        else:
            self.node[self.begin + location ] = None

    def destroy(self):
        self.node = None
        self.begin = - 1
        self.end = -1
        self.size = 0 


contiguity_list = Contiguity_list(10)
contiguity_list.insert_node(9, 666)
contiguity_list.insert_node(0, 9)
contiguity_list.insert_node(1, 8)
contiguity_list.insert_node(2, 7)
contiguity_list.insert_node(3, 6)
contiguity_list.insert_node(4, 5)
contiguity_list.insert_node(5, 4)
contiguity_list.insert_node(6, 3)
contiguity_list.insert_node(7, 2)
contiguity_list.insert_node(8, 1)

contiguity_list.locate_node(666)
contiguity_list.locate_node(3)

contiguity_list.remove_node(0)
contiguity_list.remove_node(1)
contiguity_list.remove_node(2)
contiguity_list.remove_node(3)
contiguity_list.remove_node(4)
contiguity_list.remove_node(5)
contiguity_list.remove_node(6)
contiguity_list.remove_node(7)
contiguity_list.remove_node(8)
contiguity_list.remove_node(9)

contiguity_list.show_list()

contiguity_list.insert_node(4, 1)
contiguity_list.insert_node(8, 3)

contiguity_list.show_list()

contiguity_list.destroy()
contiguity_list.show_list()
