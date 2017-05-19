from unittest import TestCase, main


def is_even(n):
    return n % 2 == 0


class Testes(TestCase):
    def test_even(self):
        self.assertTrue(is_even(2))

    def test_odd(self):
        self.assertFalse(is_even(3))


if __name__ == '__main__':
    main()
