from unittest import TestCase
from pagination import make_pagination_range

class PaginationTest(TestCase):
    # red, green e refactor
    def test_make_pagination_range_returns_pagination(self):

        pagination = make_pagination_range(
            page_range = list(range(1,12)),
            qtd_paginas = 4,
            current_page=1
        )
        self.assertEqual([1,2,3,4], pagination)

   