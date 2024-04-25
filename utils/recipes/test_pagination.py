from unittest import TestCase

class PaginationTest(TestCase):

    def test_make_pagination_range_returns_pagination(self):

        pagination = make_pagination_range(
            page_range = list(range(1,12)),
            qtd_paginas = 4
            current_page=1
        )
        self.assertIn([1,2,3,4], pagination)