def check_id_valid(id_number):
    """
    The function receives a ID and checks with is the appropriate size
    If it is the appropriate size, she multiplies the odd index by 1 and the even index by 2
    After that, if there are numbers bigger than 10, she adds them up
    Then returns true if the sum of all the numbers is divisible by 10 and false if not

    """
    id = str(id_number)
    if len(id)<9:
        return False
    else:
        id_new=[str(int(id[i]))  if i%2==0 else str(2*int(id[i])) for i in range(len(id))]
        id_add=[int(i) if len(i)==1 else int(i[0])+int(i[1]) for i in id_new ]
        return sum(id_add)%10 == 0

print(check_id_valid(123456780))
print(check_id_valid(123456782))





class IDIterator:
    """
    This class create valid ID by iter-protocol
    """
    def __init__(self,id=100000000):
        self.id=id
        self.id_index=self.id-1000000000
    def get_id(self):
        return self.id
    def __iter__(self):
        return self
    def __next__(self):
        """
        If we reach 10 digits we raise EROR StopIteration
        else as long as we get a False, we update the index and the ID
        and return the vaild ID
        """
        if self.id_index >= 0:
            raise StopIteration("You passed the 9 digits")
        else:
            self.id_index += 1
            self.id += 1
            while not check_id_valid(self.id):
                self.id += 1
                self.id_index += 1
                if self.id_index >= 0:
                    raise StopIteration("You passed the 9 digits")
        return self.id
    




def id_generator(id_number):
    """
    A generator that yields valid IDs.
    """
    while 100000000 <= id_number < 1000000000:
        id_number += 1
        while not check_id_valid(id_number):
            if id_number >=1000000000:
                return("You passed the 9 digits")
            id_number += 1
        yield id_number



def main():
    """
    Chek if the id its only from digits
    If the choice is it,
    create an object from class IDiterator and call the next method 10 times by for lop and print 10 ID vaild.
    If the choice is gen,
    call the func id_generator and by the next method in the for lop we print 10 ID vaild

    """
    while True:
        id_input = input("Enter id:")
        if id_input.isdigit():
            id_number = int(id_input)
            break
        else:
            print("Invalid input. Please enter a numeric ID.")

    choice = input("Enter Generator or Iterator? (gen/it)?:").strip().lower()


    while choice not in ["gen", "it"]:
        print("Enter only (gen/it)")
        choice = input("Enter Generator or Iterator? (gen/it)?:").strip().lower()

    if choice == 'it':
        id_iter = IDIterator(id_number)
        for _ in range(10):
            try:
                print(next(id_iter))
            except StopIteration as e:
                print(e)
                return 
               
            
    else:
        id_gen = id_generator(id_number)
        for _ in range(10):
            try:
                print(next(id_gen))
            except StopIteration as e:
                print(e)
                return 
              
           

if __name__ == '__main__':
	main()