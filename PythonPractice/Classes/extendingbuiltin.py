class Text(set):
    def duplicate(self):
        return self + self
    
class TrackableLIst(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableLIst()
list.append("1")