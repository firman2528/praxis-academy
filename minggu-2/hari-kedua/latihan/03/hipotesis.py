@given(list(floats(allow_nan=False, allow_infinity=False), min_size=1))

def test_mean(xs) :
    mean = sum(x) / len(xs)
    assert min(xs) <= mean(xs) <= max(xs)


