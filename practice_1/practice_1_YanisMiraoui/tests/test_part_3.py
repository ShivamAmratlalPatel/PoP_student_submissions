import pytest

try:
    from printer.printer import Document, Printer
except ImportError:
    pass


@pytest.mark.q3_1
def test_printer_import():
    from printer.printer import Document, Printer


@pytest.fixture
def sample_docs():
    d1 = Document(("page 1", "page 2", "page 3"))
    d2 = Document(("single page",))
    d3 = Document(
        (
            "Amet ipsum tempora est modi magnam."
            " Dolore modi consectetur ut amet. "
            "Numquam modi quiquia ipsum. Magnam "
            "dolor sed quisquam consectetur amet "
            "porro voluptatem. Modi ut sed aliquam"
            " etincidunt porro. Consectetur sit dolore ipsum."
            " Magnam sed sit velit voluptatem voluptatem "
            "adipisci adipisci. Eius sit sit dolor sed quiquia.\n",
            "Amet ipsum tempora est modi magnam."
            " Dolore modi consectetur ut amet. "
            "Numquam modi quiquia ipsum. Magnam "
            "dolor sed quisquam consectetur amet "
            "porro voluptatem. Modi ut sed aliquam"
            " etincidunt porro. Consectetur sit dolore ipsum.\n"
            " Magnam sed sit velit voluptatem voluptatem "
            "adipisci adipisci. Eius sit sit dolor sed quiquia.",
        )
    )
    return d1, d2, d3


@pytest.mark.q3_2
def test_enqueue(sample_docs):
    p = Printer()
    for d in sample_docs:
        p.enqueue(d)


@pytest.mark.q3_3
@pytest.mark.parametrize("q, val", [(1, 2), (2, 1), (3, 0)])
def test_cancel(sample_docs, q, val):
    p = Printer()
    for d in sample_docs:
        p.enqueue(d)
    for _ in range(q):
        p.cancel()
    assert len(p) == val


@pytest.mark.q3_4
@pytest.mark.parametrize("q, val", [(1, 1), (2, 2), (3, 3)])
def test_len(sample_docs, q, val):
    p = Printer()
    for d in range(q):
        p.enqueue(sample_docs[d])
    assert len(p) == val, f"expected length of {val} but got {len(p)}"


@pytest.mark.q3_5
@pytest.mark.parametrize("q, val", [(1, 3), (2, 4), (3, 6)])
def test_pages(sample_docs, q, val):
    p = Printer()
    for d in range(q):
        p.enqueue(sample_docs[d])
    assert p.pages() == val


@pytest.mark.q3_6
def test_print_remove(sample_docs):
    p = Printer()
    p1, p2, _ = sample_docs
    p.enqueue(p2)
    p.enqueue(p1)
    o = p.print()
    assert o == "single page" and (len(p) == 1 and p.pages() == 3)


@pytest.mark.q3_6
def test_print(sample_docs):
    p = Printer()
    p1, p2, _ = sample_docs
    p.enqueue(p1)
    p.enqueue(p2)
    o = p.print()
    assert o == "page 1" and (len(p) == 2 and p.pages() == 3)


@pytest.mark.q3_6
def test_print_empty(sample_docs):
    p = Printer()
    for d in sample_docs:
        p.enqueue(d)
    printed = []
    for _ in range(p.pages()):
        printed.append(p.print())
    assert (printed[3] == "single page") and not len(p), (
        f"expected an empty print queue with 4th printed page 'single page'"
        f"but got: {printed[3]}"
    )
