from pagination import Pagination
import unittest


class TestPagination(unittest.TestCase):
    def test_init(self):
        pagination = Pagination(total_data=1000, current_page=1, max_data_page=100)
        self.assertIsNotNone(pagination)

    def test_get_limit(self):
        pg1 = Pagination(total_data=1000, current_page=1, max_data_page=100)
        self.assertEqual(100, pg1.get_limit())

        pg2 = Pagination(total_data=1000, current_page=1, max_data_page=200)
        self.assertEqual(200, pg2.get_limit())

        pg3 = Pagination(total_data=1000, current_page=1, max_data_page=300)
        self.assertEqual(300, pg3.get_limit())

    def test_get_offset(self):
        pg0 = Pagination(total_data=1000, current_page=0, max_data_page=100)
        self.assertEqual(0, pg0.get_offset())

        pg1 = Pagination(total_data=1000, current_page=1, max_data_page=100)
        self.assertEqual(0, pg1.get_offset())

        pg2 = Pagination(total_data=1000, current_page=2, max_data_page=100)
        self.assertEqual(100, pg2.get_offset())

        pg3 = Pagination(total_data=1000, current_page=10, max_data_page=100)
        self.assertEqual(900, pg3.get_offset())

        pg4 = Pagination(total_data=1000, current_page=15, max_data_page=100)
        self.assertEqual(900, pg4.get_offset())

        pg5 = Pagination(total_data=0, current_page=1, max_data_page=100)
        self.assertEqual(0, pg5.get_offset())

    def test_get_total_page(self):
        pg0 = Pagination(total_data=0, current_page=1, max_data_page=100)
        self.assertEqual(0, pg0.get_total_page())

        pg1 = Pagination(total_data=1000, current_page=1, max_data_page=0)
        self.assertEqual(10, pg1.get_total_page())

        pg2 = Pagination(total_data=1000, current_page=1, max_data_page=100)
        self.assertEqual(10, pg2.get_total_page())

        pg3 = Pagination(total_data=1000, current_page=1, max_data_page=300)
        self.assertEqual(4, pg3.get_total_page())

        pg4 = Pagination(total_data=1000, current_page=1, max_data_page=1500)
        self.assertEqual(1, pg4.get_total_page())

    def test_get_pagination_page_number(self):
        pg1 = Pagination(total_data=1000, current_page=0, max_data_page=200)
        self.assertEqual([1, 2, 3], pg1.get_pagination_page_number())

        pg2 = Pagination(total_data=1000, current_page=1, max_data_page=200)
        self.assertEqual([1, 2, 3], pg2.get_pagination_page_number())

        pg3 = Pagination(total_data=1000, current_page=2, max_data_page=200)
        self.assertEqual([1, 2, 3, 4], pg3.get_pagination_page_number())

        pg4 = Pagination(total_data=1000, current_page=3, max_data_page=200)
        self.assertEqual([1, 2, 3, 4, 5], pg4.get_pagination_page_number())

        pg5 = Pagination(total_data=1000, current_page=4, max_data_page=200)
        self.assertEqual([2, 3, 4, 5], pg5.get_pagination_page_number())

        pg6 = Pagination(total_data=1000, current_page=5, max_data_page=200)
        self.assertEqual([3, 4, 5], pg6.get_pagination_page_number())

        pg7 = Pagination(total_data=1000, current_page=10, max_data_page=200)
        self.assertEqual([3, 4, 5], pg7.get_pagination_page_number())

    def test_get_pagination_dict(self):
        pg1 = Pagination(total_data=1000, current_page=1, max_data_page=100)
        expect_dict = {
            "limit": 100,
            "offset": 0,
            "current_page": 1,
            "total_page": 10,
            "page_number": [1, 2, 3],
        }
        self.assertEqual(expect_dict, pg1.get_pagination_dict())
