def isBalanced(num):
        sum_even = 0
        sum_odd = 0
        for i in range(0, len(num), 2):
            sum_even += int(num[i])
        for i in range(1, len(num), 2):
            sum_odd += int(num[i])
        if sum_odd == sum_even:
            return True
        else:
            return False