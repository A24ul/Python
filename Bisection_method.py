def square_root_bisection(number, tolerance =1e-7 , max_num_iter=100):

    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)
    print('Number: ',number)
    print('initial: ',high)
    for _ in range(max_num_iter):
        mid = (low + high) / 2
        print('Low + High / 2: ', mid)
        print('Sq of mid: ', mid ** 2)
        if mid ** 2 > number:
            high = mid
            print('High after mid assignment: ', high)
        else:
            low = mid
            print('Low after mid assignment: ', low)
        print("Sub high and low: ", high - low)
        print('Result: ', (low + high) / 2)
        print('tolerance: ', tolerance)
        if high - low <= tolerance:
            result = (low + high) / 2
            print(f"The square root of {number} is approximately {result}")
            return result

    print(f"Failed to converge within {max_num_iter} iterations")
    return None

print(square_root_bisection(16, 1e-5, 100))
#print(square_root_bisection(225, 1e-7, 100))
#print(square_root_bisection(225, 1e-7, 10))
#print(square_root_bisection(225, 1e-3, 100))
#print(square_root_bisection(81, 1e-3, 50))
#print(square_root_bisection(0.25, 1e-7, 50))
#print(square_root_bisection(0.001, 1e-7, 50))
