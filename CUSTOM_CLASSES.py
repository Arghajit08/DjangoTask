class Rectangle:
    ##Initialization(as said in first point)
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    ##Iteration according to condition mentioned in third point
    # Method to make the class iterable
    def _iter_(self):
        # Return an iterator that yields the length and width in the desired format
        return iter([{'length': self.length}, {'width': self.width}])

# Example usage:
rectangle = Rectangle(5, 10)

# Iterate over the rectangle instance
for dimension in rectangle:
    print(dimension)
