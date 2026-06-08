from pyPrac import compress, two_sum, valid_palindrome, max_subarray, nearest_exit


def run_tests():
    tests = [
        ("compress aaabbc", compress("aaabbc"), "a3b2c1"),
        ("compress a", compress("a"), "a1"),
        ("compress aaAA", compress("aaAA"), "a2A2"),

        ("two_sum basic", two_sum([2, 7, 11, 15], 9), [0, 1]),
        ("two_sum later", two_sum([3, 2, 4], 6), [1, 2]),

        ("palindrome true", valid_palindrome("A man, a plan, a canal: Panama"), True),
        ("palindrome false", valid_palindrome("race a car"), False),

        ("max_subarray mixed", max_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6),
        ("max_subarray all negative", max_subarray([-3, -2, -5]), -2),

        ("nearest_exit simple", nearest_exit([
            ["+", "+", "."],
            [".", ".", "."],
            ["+", "+", "+"]
        ], [1, 0]), 2),
    ]

    passed = 0

    for name, result, expected in tests:
        if result == expected:
            print(f"✅ {name}")
            passed += 1
        else:
            print(f"❌ {name}")
            print(f"   expected: {expected}")
            print(f"   got:      {result}")

    print(f"\nPassed {passed}/{len(tests)} tests")


if __name__ == "__main__":
    run_tests()