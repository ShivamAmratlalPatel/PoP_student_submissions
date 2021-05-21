import pytest

try:
    from printer.printer import Document
except ImportError:
    pass


@pytest.mark.q2_1
def test_printer_import():
    from printer.printer import Document


@pytest.fixture
def sample_doc():
    p1 = "Amet ipsum tempora est modi magnam. Dolore modi conssectetur amet.\n"
    " porro voluptatem. Modi ut sed aliquam etincidunt porro. Conectetur ut amet."
    " Numquam modi quiquia ipsum. Magnam dolor sed quisquam consectetur sit"
    " dolore ipsum. Magnam sed sit velit voluptatem voluptatem adipisci adipisci.\n"
    " Eius sit sit dolor sed quiquia."
    p2 = "Single lined statement"
    p3 = "Hello, world!"
    p4 = " "
    return p1, p2, p3, p4


@pytest.mark.q2_1
def test_instantiate_document(sample_doc):
    Document(sample_doc)


@pytest.mark.q2_2
def test_append(sample_doc):
    d = Document()
    for page in sample_doc:
        d.append(page)


@pytest.mark.q2_3
def test_print():
    p = ["page 1", "page 2", "page 3"]
    d = Document(p)
    x = d.print()
    y = d.print()
    assert x == "page 1" and y == "page 2", f"expected that {x} printed first, then {y}"


@pytest.mark.q2_4
@pytest.mark.parametrize(
    "a, b, val",
    [
        (1, 3, 2),
        (0, 0, 0),
        (1, 4, 3),
        (0, 4, 4),
    ],
)
def test_len(sample_doc, a, b, val):
    d = Document(sample_doc[a:b])
    assert len(d) == val, f"expected a length of {val} but got {len(d)}"
