# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
        num_1 = get_number_from_ll(l1)
        num_2 = get_number_from_ll(l2)

        s = num_1 + num_2
        new_ll = build_ll_from_number(s)
        return new_ll


def get_number_from_ll(ll):
    val_str = ''
    node = ll
    while node:
        val = node.val
        val_str += str(val)
        node = node.next
    val_str_reversed = val_str[::-1]

    return int(val_str_reversed)

def build_ll_from_number(num):
    num_str = str(num)[::-1]

    assert(len(num_str) > 0)
    root = ListNode(int(num_str[0]))
    node = root
    for digit in num_str[1:]:
        node.next = ListNode(int(digit))
        node = node.next

    return root


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8