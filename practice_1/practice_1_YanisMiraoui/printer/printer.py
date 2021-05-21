class Document:
    def __init__(self, string=[]):
        if string:
            self.string = list(string)
        else:
            self.string = []

    def append(self, string):
        self.string.append(string)

    def print(self):
        printing = self.string[0]
        self.string = self.string[1:]
        return printing

    def __len__(self):
        return len(self.string)


class Printer:
    def __init__(self):
        self.queue = []

    def enqueue(self, document):
        self.queue.append(document)

    def cancel(self):
        self.queue = self.queue[1:]

    def __len__(self):
        return len(self.queue)

    def pages(self):
        return sum(len(document) for document in self.queue)

    def print(self):
        if not self.queue[0]:
            printing = ""
        else:
            printing = self.queue[0].string[0]
        self.queue[0] = self.queue[0].string[1:]
        if len(self.queue[0]) == 0:
            self.queue = self.queue[1:]
        return printing
