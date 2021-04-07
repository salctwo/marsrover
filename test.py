from service import action

def test(title, result, expected):
    assert expected == result, title + f', expected: {expected}, but result: {result} ❌'
    print(title + ' ✅')

test('when Rover is (0,0,N) and command L result (0,0,W)',  action( (0,0,'N'), 'L'), (0,0,'W'))
test('when Rover is (1,1,S) and command M result (1,2,S)',  action( (1,1,'S'), 'M'), (1,2,'S'))
test('when Rover is (2,3,E) and command R result (2,3,S)',  action( (2,3,'E'), 'R'), (2,3,'S'))
test('when Rover is (9,1,E) and command M result (0,1,E)',  action( (9,1,'E'), 'M'), (0,1,'E'))
test('when Rover is (9,9,S) and command M result (9,0,S)',  action( (9,9,'S'), 'M'), (9,0,'S'))
