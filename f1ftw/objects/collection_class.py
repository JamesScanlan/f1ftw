class CollectionClass(object):
    def __init__(self):
        self.index=-1
        self.objects=[]
    def add_object(self, new_object):
        self.objects.append(new_object)
    def get_object_index(self, object_to_compare):
        index = 0
        for existing_object in self.objects:
            if existing_object == object_to_compare:
                return index
            else:
                index += 1
        return -1
    def upsert_object(self, object_in_question):
        index = self.get_object_index(object_in_question)
        if index > -1:
            self.objects[index] == object_in_question
        else:
            self.add_object(object_in_question)
        return self.get_object_index(object_in_question)
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index == len(self.objects):
            raise StopIteration
        self.index += 1
        return self.objects[self.index-1]
    def __len__(self):
        return len(self.objects)
    def __getitem__(self, index):
        if index > len(self.objects)-1:
            raise ValueError("Index presented greater than number of parsed objects")
        return self.objects[index]
    def __setitem__(self, index, value):
        if index > len(self.objects)-1:
            raise ValueError("Index presented greater than number of parsed objects")
        self.objects[index] = value
    def __delitem__(self, index):
        if index > len(self.objects)-1:
            raise ValueError("Index presented greater than number of parsed objects")
        del self.objects[index]
