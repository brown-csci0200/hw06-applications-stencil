from classes import ListNode, TreeNode

def equal_encoding(s1: str, s2: str) -> bool:
    """
    Given two strings s1 and s2 of equal length, determine whether they are equal under a simple 
    character-based encoding that replaces each character in s1 with another character to turn it into s2.

    Each appearance of a character in s1 must be replaced with the same character. No two characters in s1
    can be replaced with the same character in s2. A character is allowed to be replaced with itself.

    Args:
    - s1 (str): The first string.
    - s2 (str): The second string.

    Returns:
    - bool: True if the strings can be encoded as described, False otherwise.

    Time Complexity Requirement:
    - O(n), where n is the length of string s1 (and s2).

    Space Complexity Requirement:
    - O(n), where n is the length of string s1 (and s2).
    """
    pass

def sum_pair(nums: list[int], target: int) -> set[int]:
    """
    Given a sequence of numbers and a target number, return the indices (positions in the input list) 
    of the two numbers that add to the target number (in the form of a set). 
    You may assume that there is exactly one pair of indices meeting this criterion. 

    Args:
    - nums (list[int]): The input list of integers.
    - target (int): The target sum.

    Returns:
    - set[int]: A set containing the indices of the two numbers whose values sum to the target.

    Time Complexity Requirement:
    - O(n), where n is the length of the input list.

    Space Complexity Requirement:
    - O(n), where n is the length of the input list.
    """
    pass

def merge_k(lists: list[ListNode]) -> ListNode:
    """
    Given a list of sorted Singly Linked Lists, weave them together into a single sorted Singly Linked List.
    
    Retains duplicates; the length of the returned list equals the sum of the lengths of the inner input lists.

    Args:
    - lists (list[ListNode]): List of sorted Singly Linked Lists.

    Returns:
    - ListNode: The head of the merged sorted Singly Linked List.

    Time Complexity Requirement:
    - O(n * log(k)), where k is the number of input Linked Lists (i.e. the length of the outer list), 
    and n is the total number of nodes across all lists.

    Space Complexity Requirement:
    - At most O(k), where k is the number of input Linked Lists (i.e. the length of the outer list).

    For testing, you may convert list[int] to a ListNode (Singly Linked List) using the arr_to_listnode method.
    """
    pass

def ll_modes(nums_list: ListNode) -> set[int]:
    """
    Computes the mode (or modes, in case of ties) of a sorted Singly Linked List.

    Args:
    - nums_list (ListNode): The head of the sorted Singly Linked List.

    Returns:
    - set[int]: A set containing all modes of the linked list.

    For testing, you may convert list[int] to a ListNode (Singly Linked List) using the arr_to_listnode method.
    """
    pass

def bst_modes(root: TreeNode) -> set[int]:
    """
    Computes the mode (or modes, in case of ties) of a Binary Search Tree (BST).

    Args:
    - root (TreeNode): The root of the Binary Search Tree.

    Returns:
    - set[int]: A set containing all modes of the BST.

    Time Complexity Requirement:
    - O(n), where n is the total number of nodes in the BST.

    Space Complexity Requirement:
    - O(n), where n is the total number of nodes in the BST.

    For testing, you may convert list[int] to a TreeNode using the arr_to_bst method.
    """
    pass