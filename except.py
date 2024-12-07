def divider(a, b):
    if a < b:
        return ValueError("Second number can not be higher than first number")
    elif b > 100:
        return IndexError("Second number can not be more than 100")
    else:
        return a/b

print(divider(4, 2))
print(divider(4, 8))
print(divider(105, 104))


try:
    result = []
    data = [10, 2, 2, 5, 4, 18, 0, 15, 8, 4]
    for key in data:
        res = divider(key, data[key])
        result.append(res)
    print(result)
except (IndexError, ValueError):
    print("There is an index or value error in your code")
except (ZeroDivisionError):
    print("You can't divide to zero")