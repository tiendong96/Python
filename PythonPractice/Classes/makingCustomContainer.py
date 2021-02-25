class TagCloud:
    def __init__(self) -> None:
        self.__tags = {} #use prefix '__' to denote a private attribute or private methods in a class

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        iter(self.__tags)

cloud = TagCloud()
print(cloud.__dict__) #holds all the attributes in the class
print(cloud._TagCloud__tags)