# List(built-in-type) base class

class TrackList(list):

    def __init__(self, *args):
        # use all the  attributes of the list
        super().__init__(*args)
        self.add_count = 0

    def append(self, item):
        # use all the methods and override the append method of the list
        super().append(item)
        self.add_count += 1

    def extend(self, iterable):
        # use all the methods and override the extend method of the list
        super().extend(iterable)
        self.add_count += len(iterable)


tracked_list = TrackList([1, 2, 3, 4])
print(tracked_list)

tracked_list.append(6)
print(tracked_list)

tracked_list.extend([7, 8, 9])
print(tracked_list)
