# Work by Fabien AUBRET <fabien.aubret@gadzarts.org>
# For Arts et Metiers engineering school
# Published under Open Source License

# This is a custom implementation of a dictionary which is untyped
# It can handle any type of variable


class Dictionary:

    def __init__(self):
        self.dic = []

    def __len__(self):
        return len(self.dic)

    def __contains__(self, item):
        el_list = [self.dic[k][0] for k in range(len(self))]
        return item in el_list

    # Inserts given element in dictionary
    def push(self, el):
        el_list = [self.dic[k][1] for k in range(len(self))]
        max_list = 0 if len(el_list) <= 0 else max(el_list) + 1
        if el not in self:
            self.dic.append((el, max_list))

    # Remove the element with given index from dictionary
    def pop(self, index):
        del self.dic[index]

    # Returns the index of the given "index" in dictionary
    # Be aware tha dictionary index can be different of list index because of push/pop operations
    def get_by_index(self, index):
        el_list = [self.dic[k][1] for k in range(len(self))]
        return el_list.index(index)

    # Returns the index of the given element in dictionary
    def get_by_element(self, el):
        el_list = [self.dic[k][0] for k in range(len(self))]
        return el_list.index(el)

    # Shows dictionary as a list of elements
    def show_elements(self):
        el_list = [self.dic[k][0] for k in range(len(self))]
        return el_list

    # Shows dictionary as a list of indexes
    def show_indexes(self):
        el_list = [self.dic[k][1] for k in range(len(self))]
        return el_list

    # This could reduce the size of the dictionary based on the repetition of words
    def reduce(self, base_list, next_size):
        pass
