from prefix_codes import is_prefix_code
from unary_coding import unary, inverted_unary
from reduced_binary_coding import reduced_binary_coding
from minimal_binary_coding import minimal_binary_coding
from gamma_coding import gamma_coding
from delta_coding import delta_coding
from omega_coding import omega_coding
from interpolative_coding import interpolative_coding
from nibble_coding import nibble_coding, byte_coding
from golomb_coding import golomb_coding
from levenshtein_coding import levenshtein_coding


def test_is_prefix_code():
    positive = [
        [unary(i) for i in range(100)],
        [inverted_unary(i) for i in range(100)],
        [minimal_binary_coding(i, 100) for i in range(100)],
        [gamma_coding(i) for i in range(100)],
        [delta_coding(i) for i in range(100)],
        [omega_coding(i) for i in range(1, 100)],
        [levenshtein_coding(i) for i in range(100)],
        [nibble_coding(i) for i in range(100)],
        [byte_coding(i) for i in range(100)],
        [golomb_coding(i, 5) for i in range(100)]
    ]

    negative = [
        interpolative_coding(list(range(0, 100)), 0, 100),
        [reduced_binary_coding(i) for i in range(100)]
    ]

    assert all([
        is_prefix_code(p) for p in positive
    ])

    assert not any([
        is_prefix_code(n) for n in negative
    ])
