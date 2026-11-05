def nearest_smaller_to_left(arr):
    stack = []
    result = []

    for num in arr:

        while stack and stack[-1] >= num:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(num)

    return result

arr = [4, 5, 2, 10, 8]
print(nearest_smaller_to_left(arr))  