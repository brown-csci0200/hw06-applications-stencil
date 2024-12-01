from imp_hw6 import equal_encoding, sum_pair, merge_k, ll_modes, bst_modes
from classes import ListNode, TreeNode
from test_helpers import arr_to_listnode, listnode_to_arr, arr_to_bst

def test_example():
    assert 2 == 1 + 1


# Example for calling methods in imp_hw6.py
def test_example_equal_encoding():
    # Some examples from the handout (you should write tests with more!)
    assert equal_encoding("dad", "bob") == True
    assert equal_encoding("truth", "truce") == False


# Example for using linked list helpers (needed to test part 3)
def test_example_linked_list_helpers():

    # Make a linked list from a list
    single_linked_list = arr_to_listnode([1, 2, 3])

    # Example:  accessing components of the linked list
    # ListNode(1) -> ListNode(2) -> ListNode(3)
    assert 1 == single_linked_list.val
    assert 2 == single_linked_list.next.val
    assert 3 == single_linked_list.next.next.val

    # If needed for testing, can convert back to a list
    assert [1, 2, 3] == listnode_to_arr(single_linked_list)


# Example for using BST helpers (needed to test part 4)
def test_example_bst_helpers():

    # Example 1:  Make a BST from a list (matches example 1 in part 4.2 of handout)
    # (Note:  list must already be in correct order to satisfy a BST.
    #  see test_helpers.py for details.)
    bst1 = arr_to_bst([1,None,2,None,None,2])

    assert 1 == bst1.val # root
    assert None == bst1.left
    assert 2 == bst1.right.val

    # Example 2:  make a BST from a list (matches example 2 in part 4.2 of handout)
    bst2 = arr_to_bst([5,4,8,3,4,7,9])
    assert 5 == bst2.val # Root

    


# TODO:  Add more tests!
