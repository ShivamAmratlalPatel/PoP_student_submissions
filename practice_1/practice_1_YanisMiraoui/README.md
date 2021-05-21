# Principles of Programming exam practice question

## Instructions


1. Ensure your Principles of Programming venv is active.
2. Clone this repository.
3. Complete the programming tasks. Tests are provided for parts 2 and 3.
   Parts 1 and 4.1 are tested by the autograder when you push.
4. Commit and push as you go. Even if you have network issues which prevent you
   from pushing, you can still make commits locally and it is essential that
   you do. **Do not** rely on one big commit and push at the
   end of the exam. Only commits timestamped before the end of the exam
   will count.

The tests and autograder are a guide, the exam will be manually marked in order
to ensure that your code doesn`t produce the right output for the wrong reasons,
and in order to allocate the part 4.2 style marks.

## The task

Your task is to implement a class which simulates the operation of a computer
printer on documents. Each page of a document will be represented by a string
(which might contain line breaks, so it could be many paragraphs). 

Each document will be represented by a class containing a queue of pages, so that a document is built up
by appending pages, and pages can be removed to be printed by popping them from
the queue.

The printer itself will be represented by class containing queue of documents, but with a slight
twist. The documents will be added to the printer, but printing will return the
next page of the first document in the queue.

> When you need to use a queue in writing this code, you are advised to use [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque)
 
### Part 1 (2 marks)

Create a package `printer` containing a module `printer.py`. Make the package
installable. Install the package in editable mode.

### Part 2 (5 marks)

In the `printer.printer` module, create a class `Document`. The constructor of
this class should take a single optional argument, which is a sequence of
strings, representing the pages of a document. The constructor should construct
a queue out of these pages in the same order they are passed in, so that the
page in position 0 is first in the queue and the page in position -1 is the
last. If no sequence is passed in then an empty queue should be created. (2 marks)

Implement an `append()` method which should take a single string argument and
append that string as a page at the end of the `Document`. (1 mark)

Implement a `print()` method which removes the first page from the `Document`, and
returns it. (1 Mark)

Implement the `__len__()` special method on `Document` so that it returns the
number of pages currently in the document. (1 Mark)

### Part 3 (9 marks)

In the `printer.printer` module, create a class `Printer`. The constructor of
this class should take no arguments (other than the object itself) but should
create a queue to contain the documents currently waiting to be printed. The
queue should start out empty. (1 Mark)

Implement a method `enqueue()` which takes a `Document` and adds it to the end
of the print queue. (1 Mark)

Implement a method `cancel()` which removes and discards the `Document` at the
front of the print queue. (1 Mark)

Implement the `__len__()` special method for the `Printer`. This should return
the number of documents waiting to be printed. (1 Mark)

Implement a method `pages()` which returns the total number of pages in all the
documents currently in the print queue. (2 Marks)

Implement a method `print()` which removes and returns the first page of the
first `Document` on the print queue. If this makes the first `Document` empty
then that document should be removed from the print queue and discarded. (3 marks)

### Part 4 (4 marks)

1. Ensure that your code passes Flake8 (2 marks); and 
2. otherwise conforms to good programming style as we have learned in this
   course (2 marks).

There is no need to write any docstrings for this exam.
