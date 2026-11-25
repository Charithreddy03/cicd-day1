from app import add, multiply

def test_add():
    assert add(2,3) == 5

def test_multiply():
    assert multiply(2, 3) == 6

if __name__ == "__main__":
    test_add()
    test_multiply()
    print("All tests passed!")
