import random
import time


def multiply_ints(num1: str, num2: str):
    """
    Multiply two string integers
    :param num1:
    :param num2:
    :return:
    """
    # num1 and num2 are strings!
    nums_to_add = []

    # multiply
    for i in range(len(num1) - 1, -1, -1):
        val1 = int(b10(num1[i], (len(num1) - (i + 1))))

        for j in range(len(num2) - 1, -1, -1):
            val2 = int(b10(num2[j], (len(num2) - (j + 1))))

            # print(val1, val2)
            nums_to_add.append(val1 * val2)

    s = nums_to_add[0]
    for num in range(1, len(nums_to_add)):
        s = add(str(nums_to_add[num]), str(s))

    return {"values": nums_to_add, "total": s}

# add
def add(n1: str, n2: str):
    """
    Adds two string integers
    :param n1:
    :param n2:
    :return:
    """
    mx = max(len(n1), len(n2))

    n1 = pad_to(n1, mx)
    n2 = pad_to(n2, mx)

    carry = 0
    output = ["0" for _ in range(mx + 1)]

    for i in range(mx - 1, -1, -1):
        # 2,1,0
        d1 = 0
        d2 = 0

        try:
            d1 = int(n1[i])
        except:
            pass

        try:
            d2 = int(n2[i])
        except:
            pass

        total = d1 + d2 + carry
        dig = total % 10
        carry = total // 10

        output[i + 1] = str(dig)

    # add the final carry
    output[i] = str(carry)

    return int("".join(output))


def pad_to(s: str, n: int):
    """
    pads string s to length n, with 0's, adding 0's to the left side
    :param s:
    :param n:
    :return:
    """

    if len(s) < n:
        short = n - len(s)
        padding = ""

        for _ in range(short):
            padding += "0"

        return padding + s
    return s


def b10(s: str, exp: int):
    """
    Exponentiate the string number by powers of 10
    In decimal this means add 0's to the right hand side
    :param s:
    :param exp:
    :return:
    """
    extra_noughts = ""
    for i in range(exp):
        extra_noughts += "0"

    return s + extra_noughts


def test(n=20, r=1000, verbose=False):
    print(f"testing with {n * 2} random params between 1 and {r}")

    passes = 0

    nums1 = [random.randrange(r) for _ in range(n)]
    nums2 = [random.randrange(r) for _ in range(n)]

    for i in range(n):
        st = time.time()
        expected = nums1[i] * nums2[i]
        st = time.time() - st

        p1 = str(nums1[i])
        p2 = str(nums2[i])

        cs = time.time()
        out = multiply_ints(p1, p2)
        cs = time.time() - cs

        if out["total"] != expected:
            if verbose:
                print(f"test failed with params {p1}, {p2} (expected {expected}, got {out})")
        else:
            passes += 1
            if verbose:
                print(f"test passed with params {p1}, {p2} (expected {expected}, got {out['total']})")

        if verbose:
            print(f"builtin took {st}s, custom took {cs}s")

    print(f"passed {passes}/{n} tests")


test(5, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, verbose=True)
