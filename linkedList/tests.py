import unittest


from linkedList.linked_list import LinkedList


class Tests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def _fill_in_linked_list(self):
        self.linked_list.push_front(3)
        self.linked_list.push_front(2)
        self.linked_list.push_front(1)
        self.assertEqual([1, 2, 3], self.linked_list.to_list())

    def test_create(self):
        self.assertEqual(list(), list(self.linked_list))

    def test_push_front(self):
        self.linked_list.push_front(1)
        self.assertEqual([1], self.linked_list.to_list())
        self.assertEqual(1, self.linked_list.head.value)
        self.assertEqual(1, self.linked_list.back.value)
        self.assertEqual(1, len(self.linked_list))

    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.assertEqual(0, len(self.linked_list))
        self._fill_in_linked_list()
        self.assertFalse(self.linked_list.is_empty())
        self.assertEqual(3, len(self.linked_list))

    def test_push_back(self):
        self._fill_in_linked_list()
        self.linked_list.push_back(4)
        self.assertEqual([1, 2, 3, 4], self.linked_list.to_list())
        self.assertEqual(1, self.linked_list.head.value)
        self.assertEqual(4, self.linked_list.back.value)
        self.assertEqual(4, len(self.linked_list))

    def test_insert_after__successful(self):
        self._fill_in_linked_list()
        self.linked_list.insert_after(4, 2)
        self.assertEqual([1, 2, 4, 3], self.linked_list.to_list())
        self.assertEqual(1, self.linked_list.head.value)
        self.assertEqual(3, self.linked_list.back.value)
        self.assertEqual(4, len(self.linked_list))

    def test_insert_after__failed(self):
        self._fill_in_linked_list()
        with self.assertRaises(ValueError) as context:
            self.linked_list.insert_after(2, 4)

    def test_insert_before__successful(self):
        self._fill_in_linked_list()
        self.linked_list.insert_before(4, 2)
        self.assertEqual([1, 4, 2, 3], self.linked_list.to_list())
        self.assertEqual(4, len(self.linked_list))

    def test_insert_before__failed(self):
        self._fill_in_linked_list()
        with self.assertRaises(ValueError) as context:
            self.linked_list.insert_before(2, 4)

    def test_insert_before__failed_empty_list(self):
        with self.assertRaises(ValueError) as context:
            self.linked_list.insert_before(2, 4)

    def test_pop_front__successful(self):
        self._fill_in_linked_list()
        self.linked_list.pop_front()
        self.assertEqual([2, 3], self.linked_list.to_list())
        self.assertEqual(2, self.linked_list.head.value)
        self.assertEqual(3, self.linked_list.back.value)
        self.assertEqual(2, len(self.linked_list))

    def test_pop_front__failed_empty_list(self):
        with self.assertRaises(ValueError) as context:
            self.linked_list.pop_front()

    def test_remove__successful(self):
        self._fill_in_linked_list()
        self.linked_list.remove(2)
        self.assertEqual([1, 3], self.linked_list.to_list())
        self.assertEqual(1, self.linked_list.head.value)
        self.assertEqual(3, self.linked_list.back.value)
        self.assertEqual(2, len(self.linked_list))

    def test_remove__failed(self):
        self._fill_in_linked_list()
        with self.assertRaises(ValueError) as context:
            self.linked_list.remove(4)

    def test_remove__failed_empty_list(self):
        with self.assertRaises(ValueError) as context:
            self.linked_list.remove(2)

    def test_pop_back__successful(self):
        self._fill_in_linked_list()
        self.linked_list.pop_back()
        self.assertEqual([1, 2], self.linked_list.to_list())
        self.assertEqual(1, self.linked_list.head.value)
        self.assertEqual(2, self.linked_list.back.value)
        self.assertEqual(2, len(self.linked_list))

    def test_pop_back__failed_empty_list(self):
        with self.assertRaises(ValueError) as context:
            self.linked_list.pop_back()

    def test_find_value__successful(self):
        self._fill_in_linked_list()
        result = self.linked_list.find_value(2)
        self.assertIsNotNone(result)
        self.assertEqual(2, result.value)

    def test_find_value__failed(self):
        self._fill_in_linked_list()
        result = self.linked_list.find_value(5)
        self.assertIsNone(result)

    def test_reverse(self):
        self._fill_in_linked_list()
        self.linked_list.reverse()
        self.assertEqual([3, 2, 1], self.linked_list.to_list())
        self.assertEqual(3, self.linked_list.head.value)
        self.assertEqual(1, self.linked_list.back.value)

    def test_reverse_empty(self):
        self.linked_list.reverse()
        self.assertEqual(list(), self.linked_list.to_list())

    def test_len(self):
        self.assertEqual(0, len(self.linked_list))
        self._fill_in_linked_list()
        self.assertEqual(3, len(self.linked_list))
