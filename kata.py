#The task is to define a function which returns the sum of a sequence of integers
# variable sequence is defined as b(for begining), e(for end), and step.
# if begining value is greater than the end,function needs to return 0

EXAMPLES:
sequenceSum(2,1,2) === 2 #start, stop, step
sequenceSum(1,5,2) === 9 // 1 + 3 + 5
sequenceSum(2,3,1) === 5 // 2 + 3
sequenceSum(1,7,2) === 16 // 1 + 3 + 5 + 7

TEST CASES:
Test.describe("Basic tests")
Test.assert_equals(sequence_sum(2, 1, 2), 2)
Test.assert_equals(sequence_sum(1,5,2), 9)
Test.assert_equals(sequence_sum(2, 3, 1), 5)
Test.assert_equals(sequence_sum(1,7,2), 16)


def sequence_sum(b_number, e_number, step):
    b_number = int(b_number)
    e_number = int(e_number)
    step = int(step)
    if b_number > e_number:
        return 0
    else:
        i = (e_number - b_number) / step
        i = int(i)
        ans = 0
        for j in range(i+1):
            ans = ans + b_number
            b_number += step
        return ans
