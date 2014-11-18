#!python2
# Tui Popenoe
# string_reverse.py


def string_reverse(string):
    return string[::-1]


def main():
    print(string_reverse(raw_input("Enter a string to reverse: ")))


def test_string_reverse():
    assert string_reverse('tui') == 'iut'
    assert string_reverse('popenoe') == 'eonepop'
    assert string_reverse('solos') == 'solos'
    print('Test test_string_reverse passed.')


if __name__ == '__main__':
    test_string_reverse()
    main()
