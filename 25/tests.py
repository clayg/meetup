from argparse import Namespace
import contextlib
import io
import sys
import unittest
from unittest import mock

from main import fib, find_length, main, parser


class TestFib(unittest.TestCase):

    def test_fib_base_case(self):
        self.assertEqual(0, fib(0))
        self.assertEqual(1, fib(1))
        self.assertEqual(1, fib(2))

    def test_fib_values(self):
        expected = {
            3: 2,
            4: 3,
            5: 5,
            8: 21,
            12: 144,
        }
        for n, e in expected.items():
            self.assertEqual(e, fib(n))

    def test_small_length(self):
        expected = {
            3: 12,
        }
        for n, e in expected.items():
            self.assertEqual(e, find_length(n))

    def test_solution(self):
        self.assertEqual(4782, find_length(1000))

    def test_main_with_n(self):
        stub = Namespace(n=3)
        out = io.StringIO()
        with mock.patch.object(parser, 'parse_args', return_value=stub), \
                contextlib.redirect_stdout(out):
            main()


if __name__ == "__main__":
    sys.exit(unittest.main())
