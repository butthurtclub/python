# Python
Всем успехов.
## Installation
### Python 3.6.5
###### Windows:
[Установка Python для Windows](https://docs.python.org/3.6/using/windows.html)
###### Mac OS X:
1. Качаем Python 3.6.5 [по этой ссылке](https://www.python.org/ftp/python/3.6.5/python-3.6.5-macosx10.9.pkg)
2. Устанавливаем 
###### Ubuntu:
```bash
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev  libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
sudo tar xzf Python-3.6.5.tgz
cd Python-3.6.5
sudo ./configure --enable-optimizations
sudo make altinstall
```
### PIP
###### Для всех ОС:
[Инструкции по установке PIP](https://pip.pypa.io/en/latest/installing/)
### IDE
Качаем, устанавливаем [PyCharm IDE](https://www.jetbrains.com/pycharm/) от JetBrains. Community Edition бесплатная.
## Reading
### Python
1. [Dive Into Python 3](http://www.diveintopython3.net/index.html) Читаем 1-16 главу, попутно повторяем все примеры.
2. [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
3. [Python Data Model](https://docs.python.org/3.6/reference/datamodel.html) Разделы 3.1, 3.2, 3.3
4. [Python Built-in Types](https://docs.python.org/3.6/library/stdtypes.html)
5. [Python Control Flow Tools](https://docs.python.org/3.6/tutorial/controlflow.html)
6. [Python Data Structures](https://docs.python.org/3.6/tutorial/datastructures.html)
6. [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
7. [PEP 255 -- Simple Generators](https://www.python.org/dev/peps/pep-0255/) Опционально, ибо сложно
8. [Python time module](https://docs.python.org/3.6/library/time.html)
9. [Python Date and Time](https://docs.python.org/3.6/library/datetime.html)
10. [Python os module](https://docs.python.org/3.6/library/os.html) Просто смотрим, что есть в Python для работы с ОС
11. [Python Object-oriented filesystem paths](https://docs.python.org/3.6/library/pathlib.html)
12. [Менеджеры контекста в Python](https://habrahabr.ru/post/196382/) 
13. [Декораторы. Часть 1](https://habrahabr.ru/post/141411/)
14. [Декораторы. Часть 2](https://habrahabr.ru/post/141501/)
15. [import. Часть 1](http://asvetlov.blogspot.com/2010/05/blog-post.html)
16. [import. Часть 2](http://asvetlov.blogspot.com/2010/05/2.html)
17. [Исключения в Python](https://docs.python.org/3.6/tutorial/errors.html)
### Other
1. [JSON](https://www.tutorialspoint.com/json/index.htm)
2. [YAML](http://yaml.org/spec/1.2/spec.pdf)
## Coding
###### Подход 1:
1. Заходим в [этот раздел форума](https://my.devclub.com/forum/index.php?showtopic=7450)
2. Делаем на Python задачи Point, Car, Unit

###### Подход 2:
1. Получаем [Знание 1](https://docs.python.org/3/library/unittest.html)
2. Получаем [Знание 2](http://pythontesting.net/framework/unittest/unittest-introduction/)
3. Пишем тесты для задач Point, Car, Unit

###### Подход 3:
1. Получаем [Знание 1](https://www.python.org/dev/peps/pep-0257/)
2. Получаем [Знание 2](http://docs.python-guide.org/en/latest/writing/documentation/)
3. Пишем документацию для задач Point, Car, Unit

## Examples and Explanations
###### Требования к задачам:
1. Код должен быть оформлен в соответствии с [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
2. Код должен быть документирован.
3. Кода должен быть покрыт тестами на 100%.

###### Пример того, как должна быть выполнена и оформлена задача:
```python
__author__ = 'caiman'


import json
import unittest

__all__ = (
    'Field',
)


class Field:
    """
    A class for typed data representing.
    Supproted types: integer, floating, string.

    Usage:
    >>> field = Field('integer', 10)
    >>> field.value
    10
    >>> field.value = 42
    >>> field2 = Field('integer', 30)
    >>> field == field2
    False
    >>> field2 > field
    False
    >>> field2 < field
    True
    >>> Field.supported_types()
    ['integer', 'floating', 'string']
    >>> field.field_type
    'integer'
    """

    class FieldType:
        """
        Field constants.
        """

        integer = 'integer'
        floating = 'floating'
        string = 'string'

        all_types = [integer, floating, string]

        validators = {
            integer: int,
            floating: float,
            string: str
        }

    @classmethod
    def supported_types(cls):
        return cls.FieldType.all_types

    def _validate(self, value):
        """
        Data type validator.

        :param value: Value to validate
        :type value: int, float, str
        :raise ValueError: If value type is unsupported
        :rtype: int, str, float
        :return: Validated value
        """

        try:
            return self.FieldType.validators[self.field_type](value)
        except ValueError as e:
            raise e

    def __init__(self, field_type, value):
        """
        The initializer.

        :param field_type: Data type. Possible values: integer, float, srting.
        :type field_type: str
        :param value: Field value.
        :type value: int, float, str
        :raises ValueError, TypeError: On unsupported value or Field type.
        """

        if field_type not in self.FieldType.all_types:
            raise TypeError(f'Unsupported field type: {field_type}')

        self._field_type = field_type
        self._value = self._validate(value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'{self.field_type.capitalize()}({self.value})'

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    @property
    def field_type(self):
        return self._field_type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self._validate(value)

    def to_json(self):
        """
        JSON representation

        :return: JSON string
        :rtype: str
        """

        return json.dumps({'field_type': self.field_type, 'value': self.value})

    @classmethod
    def to_python(cls, data):
        """
        Conversion from JSON to Field

        :param data: JSON string
        :type data: str
        :raises TypeError, ValueError: On unsupported value or Field type.
        :return: Field object
        :rtype: Field
        """

        data = json.loads(data)
        return cls(**data)


class TestField(unittest.TestCase):
    def test_supported_types(self):
        self.assertEqual(
            Field.supported_types(),
            ['integer', 'floating', 'string']
        )

    def test_field_type(self):
        self.assertEqual(Field.FieldType.integer, 'integer')
        self.assertEqual(Field.FieldType.floating, 'floating')
        self.assertEqual(Field.FieldType.string, 'string')
        self.assertEqual(
            Field.FieldType.all_types,
            ['integer', 'floating', 'string']
        )
        self.assertEqual(
            Field.FieldType.validators,
            {'integer': int, 'floating': float, 'string': str}
        )

    def test_validation(self):
        x = Field('integer', 5)
        y = Field('floating', 10.0)
        z = Field('string', 'alpha')

        self.assertEqual(x._validate(10), 10)
        self.assertEqual(x._validate(10.0), 10)
        self.assertEqual(x._validate('10'), 10)
        with self.assertRaises(ValueError):
            x._validate('alpha')

        self.assertEqual(y._validate(10), 10.0)
        self.assertEqual(y._validate(10.0), 10.0)
        self.assertEqual(y._validate('10'), 10.0)
        with self.assertRaises(ValueError):
            y._validate('alpha')

        self.assertEqual(z._validate(10), '10')
        self.assertEqual(z._validate(10.0), '10.0')
        self.assertEqual(z._validate('hello'), 'hello')

    def test_init(self):
        with self.assertRaises(TypeError):
            x = Field('double', 10.5)

        with self.assertRaises(ValueError):
            x = Field('integer', 'test')

        x = Field('string', 'hello')
        self.assertEqual(x.field_type, 'string')
        self.assertEqual(x.value, 'hello')

    def test_integer(self):
        x = Field('integer', 10)

        self.assertEqual(x.field_type, 'integer')
        self.assertEqual(x.value, 10)

        x.value = 42
        self.assertEqual(x.value, 42)

        with self.assertRaises(ValueError):
            x.value = 'test'

    def test_floating(self):
        x = Field('floating', 1.5)

        self.assertEqual(x.field_type, 'floating')
        self.assertEqual(x.value, 1.5)

        x.value = 10.1
        self.assertEqual(x.value, 10.1)

        x.value = 5
        self.assertEqual(x.value, 5.0)

        with self.assertRaises(ValueError):
            x.value = 'test'

    def test_string(self):
        x = Field('string', 'test')

        self.assertEqual(x.field_type, 'string')
        self.assertEqual(x.value, 'test')

        x.value = 'Lorem ipsum'
        self.assertEqual(x.value, 'Lorem ipsum')

        x.value = 5
        self.assertEqual(x.value, '5')

    def test_operators(self):
        x = Field('integer', 10)
        y = Field('integer', 5)
        z = Field('floating', 10.0)

        self.assertTrue(x != y)
        self.assertFalse(x == y)
        self.assertTrue(x == z)
        self.assertFalse(x != z)
        self.assertTrue(x > y)
        self.assertTrue(x >= y)
        self.assertTrue(y <= x)
        self.assertTrue(y < x)
        self.assertFalse(x > z)
        self.assertFalse(x < z)
        self.assertTrue(x >= z)
        self.assertTrue(x <= z)

        y.value = 10
        self.assertTrue(x == y)
        self.assertFalse(x != y)

        s1 = Field('string', 'alpha')
        s2 = Field('string', 'bravo')

        self.assertTrue(s1 != s2)
        self.assertFalse(s1 == s2)

        s2.value = 'alpha'
        self.assertTrue(s1 == s2)
        self.assertFalse(s1 != s2)

    def test_presentation(self):
        x = Field('integer', 5)
        y = Field('floating', 10.0)
        z = Field('string', 'alpha')

        self.assertEqual(str(x), '5')
        self.assertEqual(repr(x), 'Integer(5)')

        self.assertEqual(str(y), '10.0')
        self.assertEqual(repr(y), 'Floating(10.0)')

        self.assertEqual(str(z), 'alpha')
        self.assertEqual(repr(z), 'String(alpha)')

    def test_conversion(self):
        x = Field('integer', 10)

        self.assertEqual(x.to_json(), '{"field_type": "integer", "value": 10}')

        y = Field.to_python('{"field_type": "integer", "value": 10}')
        self.assertEqual(y.field_type, 'integer')
        self.assertEqual(y.value, 10)

        with self.assertRaises(TypeError):
            Field.to_python('{"field_type": "double", "value": 10}')

        with self.assertRaises(ValueError):
            Field.to_python('{"field_type": "integer", "value": "test"}')


if __name__ == '__main__':
    unittest.main()
```
