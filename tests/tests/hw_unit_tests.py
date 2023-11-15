from unittest import TestCase
from tests.hw_tests_data import same_names, unique_names, top_names


class TestDataCollections(TestCase):
    def test_samenames(self):
        expected = 'На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, Максим Батырев, Максим Воронцов, Сергей Индюков, Сергей Сердюк'
        result = same_names()
        self.assertEqual(result, expected)


    def test_uniquenames(self):
        expected = 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
        result = unique_names()
        self.assertEqual(result, expected)

    def test_topnames(self):
        expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        result = top_names()
        self.assertEqual(result, expected)

    def test_unique_names_empty(self):
        expected = 'Уникальные имена преподавателей: '
        result = unique_names()
        self.assertNotEqual(result, expected)

    def test_same_names_empty(self):
        expected = 'На курсе Java-разработчик с нуля есть тёзки: '
        result = same_names()
        self.assertNotEqual(result, expected)

    def top_names_empty(self):
        expected = ''
        result = top_names()
        self.assertNotEqual(result, expected)