#!python2
# Tui Popenoe
# count_vowels.py


vowels = {'a': 0,
          'e': 0,
          'i': 0,
          'o': 0,
          'u': 0
          }


def count_vowels(string):
    count = 0
    vowels_counted = vowels.copy()
    for i in string:
        if i in vowels.keys():
            count += 1
            vowels_counted[i] += 1
    print('Total number of vowels: ', count)
    print('Vowel Counts: ')
    for j in vowels:
        print(j, vowels_counted[j])
    return count


def test_count_vowels():
    assert count_vowels('aeiou') == 5
    assert count_vowels('12345') == 0
    print('Test test_count_vowels passed')


def main():
    test_count_vowels()
    count_vowels(raw_input('Enter a string to count the vowels: '))


if __name__ == '__main__':
    main()
