# Define class MyFirstClass
class MyFirstClass():
    print('Hongbo Wei wrote this.')
    # Define string variable called index
    index = 'Author-Book'
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # variable + “ wrote the book: ” + variable
        print(self.index)
        print(philosopher + ' wrote the book: ' + book)
        

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list('Sun Tzu', 'The Art of War')
