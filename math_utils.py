def calculate_total(*args):
    return sum(args)

if __name__ == "__main__":
    assert calculate_total(2, 2) == 4, 'Math test failed! Expected 4.'
    print("All tests passed.")