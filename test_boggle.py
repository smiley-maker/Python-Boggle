''' Module test_boggle.py '''
import pytest
from project03 import new_board, board_to_string, board_has_word, adjacent_cells, cells_with_letter
#import project03

def test_new_board():
    b = new_board()
    assert len(b) == 4
    for a in b:
        assert len(a) == 4
        for c in a:
            assert c.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def test_board_to_string():
    b = [["A", "B", "C", "D"],
         ["E", "F", "G", "H"],
         ["I", "J", "K", "L"],
         ["M", "N", "O", "P"]]
    result = board_to_string(b)
    assert result == "[A] [B] [C] [D]\n[E] [F] [G] [H]\n[I] [J] [K] [L]\n[M] [N] [O] [P]"

def test_board_has_word():
    b = [["A", "B", "C", "D"],
         ["E", "F", "G", "H"],
         ["I", "J", "K", "L"],
         ["M", "N", "O", "P"]]
    assert board_has_word(b, "AFKGH")
    assert not board_has_word(b, "AFKGH", [(0, 0)])
    assert not board_has_word(b, "Q")
    assert not board_has_word(b, "AFKM")
    assert not board_has_word(b, "AEIE")

def test_adjacent_cells():
    current_cell = (1, 0)
    result = adjacent_cells(current_cell)
    assert set(result) == set([(0, 0), (1, 1), (2, 0), (2, 1), (0, 1)])

def test_cells_with_letter():
    b = [["A", "B", "C", "D"],
         ["E", "F", "G", "X"],
         ["I", "J", "K", "L"],
         ["X", "N", "O", "P"]]
    assert cells_with_letter(b, "A") == [(0, 0)]
    assert cells_with_letter(b, "O") == [(2, 3)]
    assert set(cells_with_letter(b, "X")) == set([(3, 1), (0, 3)])
