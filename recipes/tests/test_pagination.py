from unittest import TestCase
from .pagination import make_pagination_range

class PaginationTest(TestCase):
    # red, green e refactor
    def test_make_pagination_range_returns_pagination(self):

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=1
        )['pagination']
        self.assertEqual([1,2,3], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=2
        )['pagination']
        self.assertEqual([1,2,3,4], pagination)

        
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=3
        )['pagination']
        self.assertEqual([2,3,4,5], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=4
        )['pagination']
        self.assertEqual([3,4,5,6], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=10
        )['pagination']
        self.assertEqual([9,10,11,12], pagination)

    def test_make_pagination_range_is_static(self):
        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=18
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=19
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=20
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)

        pagination = make_pagination_range(
            page_range = list(range(1,21)),
            qty_pages = 4,
            current_page=21
        )['pagination']
        self.assertEqual([17,18,19,20], pagination)
   