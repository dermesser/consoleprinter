#!/usr/bin/env python3
# coding=utf-8
"""
console

Active8 (05-03-15)
license: GNU-GPL2
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from future import standard_library

import base64

from unittester import *
from consoleprinter import *


def printb64(s):
    """
    @type s: str
    @return: None
    """
    bs = gb64(s)
    print(bs)


class AA(object):
    """
    AA
    """
    m_float = 8.0
    m_string = "hello"
    m_int = 8

    @staticmethod
    def foo():
        """
        foo
        """
        pass

    def __str__(self):
        """
        __str__
        """
        return "AA'tje"


class ConsoleTest(unittest.TestCase):

    def test_slugify(self):
        """
        test_slugify
        """
        self.assertEqual(slugify("Hello€€€WorldFoo BarMy file.xls"), "hello4oks4oks4oksworldfooiabarmyiafile.xls")
        self.assertEqual(slugify("Hello€€€WorldFoo Bar"), "hello4oks4oks4oksworldfooiabar")
        self.assertEqual(slugify("Hello 7234 Foobar-World2"), "helloia7234iafoobar-world2")
        self.assertEqual(slugify("Hello WorldFoo Bar"), "helloiaworldfooiabar")
        self.assertEqual(slugify("yUo Xnm*a"), "yuoiaxnmkga")
        self.assertEqual(slugify("FiNNaI%y~foo"), "finnaijqy~foo")
        self.assertEqual(slugify("yGg5C4eBG"), "ygg5c4ebg")
        self.assertEqual(slugify("Y1fWg@79t"), "y1fwgqa79t")
        self.assertEqual(slugify("0f)5m@t0nS"), "0fkq5mqat0ns")
        self.assertEqual(slugify("8Q#a5devJ6r"), "8qiwa5devj6r")
        self.assertEqual(slugify("cHXE*Ya ueme"), "chxekgyaiaueme")
        self.assertEqual(slugify("JKBnvMkKK^2"), "jkbnvmkkkxg2")
        self.assertEqual(slugify("$RdoI1ghgqQf"), "jardoi1ghgqqf")
        self.assertEqual(slugify("^4OF7YXm0lCi8_t+"), "xg4of7yxm0lci8_tkw")
        self.assertEqual(slugify("Y3NtOAFlHNlvoW3QwCd"), "y3ntoaflhnlvow3qwcd")
        self.assertEqual(slugify("xWn EQ#(bbj9+^&9xuOj"), "xwniaeqiwkabbj9kwxgjg9xuoj")
        self.assertEqual(slugify("cO^I0Dt@X&1*sfIvUxCA"), "coxgi0dtqaxjg1kgsfivuxca")
        self.assertEqual(slugify("d89p8o3*iI2+6bWd1CX@1"), "d89p8o3kgii2kw6bwd1cxqa1")
        self.assertEqual(slugify("Ks68l6MN9On3GcAMfnB6t"), "ks68l6mn9on3gcamfnb6t")
        self.assertEqual(slugify("X8+y&yKigfmpKE_F0Eoxwf"), "x8kwyjgykigfmpke_f0eoxwf")
        self.assertEqual(slugify("oaJWpypbhFr+zLRL4*weU$"), "oajwpypbhfrkwzlrl4kgweuja")
        self.assertEqual(slugify("i(C + FUKV$7m(W@KnzbA"), "ikaciakwiafukvja7mkawqaknzba")
        self.assertEqual(slugify("k0ruekX#F81q^ Qso1wasbMhePv)4"), "k0ruekxiwf81qxgiaqso1wasbmhepvkq4")
        self.assertEqual(slugify("Za_SDw7y!#Q0N$XU2PXkZKQBHEM*INn"), "za_sdw7yiqiwq0njaxu2pxkzkqbhemkginn")
        self.assertEqual(slugify("@FI0Rl%C%+VBBqpv4us&eV(wVp5L9ac"), "qafi0rljqcjqkwvbbqpv4usjgevkawvp5l9ac")
        self.assertEqual(slugify("^7oS1ngoY5XTzOp@K_&fV27dUa)rXu1"), "xg7os1ngoy5xtzopqak_jgfv27duakqrxu1")
        self.assertEqual(slugify("GD31vDpPVS9eC4t@XyRS9#^$fSK8Ikv"), "gd31vdppvs9ec4tqaxyrs9iwxgjafsk8ikv")
        self.assertEqual(slugify("Saa1N%irJhxRtJ)@TeyvCPe(3MY0_GxrPq"), "saa1njqirjhxrtjkqqateyvcpeka3my0_gxrpq")
        self.assertEqual(slugify("8+HMg%*#+BI5G2Q W6zIdUZetfExAf7%4I4nw"), "8kwhmgjqkgiwkwbi5g2qiaw6ziduzetfexaf7jq4i4nw")
        self.assertEqual(slugify("dMCAMmK+6pQSVzB4%8@nbg*(yaIYrCMXOTr0eh"), "dmcammkkw6pqsvzb4jq8qanbgkgkayaiyrcmxotr0eh")
        self.assertEqual(slugify("E5O$zBLa%gw+B1deX 5a)n0@mHp$x2Zr7+YV2SQf_"), "e5ojazblajqgwkwb1dexia5akqn0qamhpjax2zr7kwyv2sqf_")
        self.assertEqual(slugify("o #9 0taChMxv8uh&TLDX4KbczB80M(wGrgPlsWYMkEsq 0Q3Id"), "oiaiw9ia0tachmxv8uhjgtldx4kbczb80mkawgrgplswymkesqia0q3id")
        self.assertEqual(slugify("GDRp6o#O(2RfG%hpB%6wL1u5+21DIJsg&6E%t6 is5Rgtpy^p1^h_s"), "gdrp6oiwoka2rfgjqhpbjq6wl1u5kw21dijsgjg6ejqt6iais5rgtpyxgp1xgh_s")
        self.assertEqual(slugify("Nl_#SQxRJ(G)NN328P8D!DuVVHn@f6OlQT9Lnup1ZkHo5ZyaJxK2&5R^R0Li74"), "nl_iwsqxrjkagkqnn328p8diqduvvhnqaf6olqt9lnup1zkho5zyajxk2jg5rxgr0li74")

    def test_stack_trace(self):
        """
        test_stack_trace
        """
        stack = stack_trace()

        self.assertTrue(str("tests.py") in stack)

    def test_fpath_in_stack(self):
        """
        test_fpath_in_stack
        """
        self.assertTrue(fpath_in_stack("tests.py"))
        self.assertFalse(fpath_in_stack("website"))

    def test_timestamp_to_string(self):
        """
        test_timestamp_to_string
        """
        option1 = "Jul 24 2013 23:14:30"
        option2 = "Jul 25 2013 06:14:30"
        option3 = "Jul 24 2013 20:14:30"
        val = timestamp_to_string_gmt(1374732870.483823)
        checked = val in [option1, option2, option3]

        self.assertTrue(checked)

    def test_exist(self):
        """
        test_exist
        """
        self.assertFalse(exist(""))
        self.assertFalse(exist(None))
        self.assertFalse(exist(False))
        self.assertFalse(exist("false"))
        self.assertFalse(exist("false"))
        self.assertTrue(exist("hello"))
        self.assertTrue(exist([1, 2]))
        self.assertTrue(exist({1, 2}))
        self.assertTrue(exist((1, 2)))
        self.assertTrue(exist(True))
        self.assertTrue(exist(1))
        self.assertTrue(exist(1.0))
        self.assertFalse(exist(False))
        self.assertFalse(exist(0))
        self.assertFalse(exist(0.0))
        self.assertFalse(exist([]))
        self.assertFalse(exist(set()))
        self.assertFalse(exist(tuple()))

        o = None

        self.assertFalse(exist(o))

        o = SystemGlobals()
        self.assertTrue(exist(o))

    def test_strcmp(self):
        """
        test_strcmp
        """
        self.assertFalse(strcmp("hello", "world"))
        self.assertTrue(strcmp("hello", "hello "))

    def test_console(self):
        """
        test_console
        """
        s = console("hello world", retval=True)

        self.assert_equal_b64(s, b'MC4wMCB8IHRlc3RzLnB5OjE5MxtbMG0bWzMwbSB8IBtbMG0bWzBtaGVsbG8gd29ybGQbWzBt\n')

        colors = ['black', 'blue', 'cyan', 'default', 'green', 'grey', 'magenta', 'orange', 'red', 'white', 'yellow', 'darkyellow']
        checks = [
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbOTBtG1szMG0gfCAbWzBtG1s5MG1ibGFjaxtbMG0=\n',
            b'MC4wMSB8IHRlc3RzLnB5OjI0NxtbOTRtG1szMG0gfCAbWzBtG1s5NG1ibHVlG1swbQ==\n',
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbMzZtG1szMG0gfCAbWzBtG1szNm1jeWFuG1swbQ==\n',
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbMG0bWzMwbSB8IBtbMG0bWzBtZGVmYXVsdBtbMG0=\n',
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbMzJtG1szMG0gfCAbWzBtG1szMm1ncmVlbhtbMG0=\n',
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbMzBtG1szMG0gfCAbWzBtG1szMG1ncmV5G1swbQ==\n',
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbMzVtG1szMG0gfCAbWzBtG1szNW1tYWdlbnRhG1swbQ==\n',
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbOTFtG1szMG0gfCAbWzBtG1s5MW1vcmFuZ2UbWzBt\n',
            b'MC4wMCB8IHRlc3RzLnB5OjIwORtbMzFtG1szMG0gfCAbWzBtG1szMW1yZWQbWzBt\n',
            b'MC4wMSB8IHRlc3RzLnB5OjIwORtbOTdtG1szMG0gfCAbWzBtG1s5N213aGl0ZRtbMG0=\n',
            b'MC4wMSB8IHRlc3RzLnB5OjIwORtbMzNtG1szMG0gfCAbWzBtG1szM215ZWxsb3cbWzBt\n',
            b'MC4wMSB8IHRlc3RzLnB5OjIwORtbOTNtG1szMG0gfCAbWzBtG1s5M21kYXJreWVsbG93G1swbQ==\n']

        cnt = 0

        for color in colors:
            res = console(color, color=color, retval=True)
            self.assert_equal_b64(res, checks[cnt])

            cnt += 1

        s = ""

        for color in colors:
            s += console(color, color=color, plainprint=True, retval=True)

        self.assert_equal_b64(s, b'G1s5MG1ibGFjaxtbMG0bWzk0bWJsdWUbWzBtG1szNm1jeWFuG1swbRtbMG1kZWZhdWx0G1swbRtb\nMzJtZ3JlZW4bWzBtG1szMG1ncmV5G1swbRtbMzVtbWFnZW50YRtbMG0bWzkxbW9yYW5nZRtbMG0b\nWzMxbXJlZBtbMG0bWzk3bXdoaXRlG1swbRtbMzNteWVsbG93G1swbRtbOTNtZGFya3llbGxvdxtb\nMG0=\n')

        return

    def test_warning(self):
        """
        test_warning
        """
        s = console_warning("Warning", retval=True)
        self.assert_equal_b64(s, b'MC4wMhtbMzFtG1szMW0gfCAbWzBtG1szMW09PRtbMG0bWzMxbSB8IBtbMG0bWzBtV2FybmluZxtb\nMzFtG1szMW0gfCAbWzBtG1szMW1GaWxlICIvVXNlcnMvcmFic2hha2VoL3dvcmtzcGFjZS9waXAv\nY29uc29sZXByaW50ZXIvdGVzdHMucHkiLCBsaW5lIDE5OCAodGVzdF93YXJuaW5nKRtbMG0bWzMx\nbSB8IBtbMG0bWzBtPT0bWzBt\n')

    def assert_equal_b64(self, s, b):
        """
        @type s: str
        @type b: bytes
        @return: None
        """
        ts = s
        s = s.split("|")[2:]
        s2 = db64(b).split("|")[2:]
        if s != s2:
            print("-- not equal --")
            printb64(ts)
            print("---------------")

        self.assertEqual(s, s2)

    def test_reversed_keywordparam(self):
        """

        #     test_reversed_keywordparam
        """

        # console("next line should be foobar")
        s = console(color="red", msg="foobar", retval=True)
        self.assert_equal_b64(s, b'MC4wMCB8IHRlc3RzLnB5OjIyOBtbMzFtG1szMG0gfCAbWzBtG1szMW1mb29iYXIbWzBt\n')

    def test_console_dict(self):
        """
        test_console_dict
        """
        d = {"val1": 10,
             "val2": 100.32,
             "val3": "hello world",
             "val4": {"val5": 88,
                      "val6": 10.32,
                      "val7": "foo bar",
                      "val8": True,
                      "val9": False}}

        s = consoledict(d, retval=True)
        self.assert_equal_b64(

            s,
            b'G1szMm1bTWFyIDE5IDIwMTUgMTA6MDE6MDJdIHwgdGVzdHMucHk6MjU4IC0gY29uc29sZWRpY3Q6\nG1swbQobWzM1bXZhbDE6IBtbMG0bWzM2bTEwG1swbQobWzM1bXZhbDI6IBtbMG0bWzkxbTEwMC4z\nMhtbMG0KG1szNW12YWwzOiAbWzBtG1szM21oZWxsbyB3b3JsZBtbMG0KG1szNW12YWw0OgobWzBt\nICAgIBtbMzVtdmFsNTogG1swbRtbMzZtODgbWzBtCiAgICAbWzM1bXZhbDY6IBtbMG0bWzkxbTEw\nLjMyG1swbQogICAgG1szNW12YWw3OiAbWzBtG1szM21mb28gYmFyG1swbQogICAgG1szNW12YWw4\nOiAbWzBtG1szMm1UcnVlG1swbQogICAgG1szNW12YWw5OiAbWzBtG1szMW1GYWxzZRtbMG0=\n')

        s = consoledict(d, retval=True, plainprint=True)
        self.assert_equal_b64(s, b'W01hciAxOSAyMDE1IDEwOjAyOjM5XSB8IHRlc3RzLnB5OjI2MiAtIGNvbnNvbGVkaWN0Ogp2YWwx\nOiAxMAp2YWwyOiAxMDAuMzIKdmFsMzogaGVsbG8gd29ybGQKdmFsNDoKICAgIHZhbDU6IDg4CiAg\nICB2YWw2OiAxMC4zMgogICAgdmFsNzogZm9vIGJhcgogICAgdmFsODogVHJ1ZQogICAgdmFsOTog\nRmFsc2U=\n')

    def test_camel_case(self):
        """
        test_camel_case
        """
        test = "hello world"
        self.assertEqual(camel_case(test), "HelloWorld")

        test = "hello_world"
        self.assertEqual(camel_case(test), "HelloWorld")

        test = "helloWorld"
        self.assertEqual(camel_case(test), "HelloWorld")

        test = "hello World"
        self.assertEqual(camel_case(test), "HelloWorld")

        test = "Hello World"
        self.assertEqual(camel_case(test), "HelloWorld")

        test = "HelloWorld"
        self.assertEqual(camel_case(test), "HelloWorld")

        test = "hello__world"
        self.assertEqual(camel_case(test), "HelloWorld")

    def test_snake_case(self):
        """
        test_snake_case
        """
        test = "hello_world"
        self.assertEqual(snake_case(test), "hello_world")

        test = "hello world"
        self.assertEqual(snake_case(test), "hello_world")

        test = "helloWorld"
        self.assertEqual(snake_case(test), "hello_world")

        test = "HelloWorld"
        self.assertEqual(snake_case(test), "hello_world")

        test = "Hello world"
        self.assertEqual(snake_case(test), "hello_world")

        test = "Hello_world"
        self.assertEqual(snake_case(test), "hello_world")

    def test_print_object_table(self):
        """
        test_print_object_table
        """
        foo = Foobar("test_print_object_table")
        self.assertTrue("mvar                               property" in console(foo, retval=True))

        res = console(foo, retval=True)
        self.assert_equal_b64(

            res.replace("tests", "__main__"),
            b'MC4wMCB8IHRlc3RzLnB5OjI5ORtbMG0bWzMwbSB8IBtbMG0bWzBtG1szMG08X19tYWluX18uRm9v\nYmFyIG9iamVjdD46IBtbMzRtRm9vYmFyIGNsYXNzG1swbQogICAgG1s5MW0gfCBGb29iYXIgICAg\nICAgICAgICAgICAgICAgICAgICAgICAgdHlwZSAgICAgICAgICAgICAgICAgICAgICAgICAgIHZh\nbHVlG1swbQogICAgG1szMG0gfCAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0bWzBt\nCiAgICAbWzMwbSB8IBtbMG0bWzMxbV9fcHJpdmF0ZXZhchtbMG0bWzMzbSAgICAgICAgICAgICAg\nICAgICAgICBpbnQgICAgICAgICAgICAgICAgICAgICAgICAgICAgG1s5Nm03NxtbMG0KG1swbSAg\nICAbWzMwbSB8IBtbMG0bWzk2bWhlbGxvICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmdW5j\ndGlvbgobWzBtICAgIBtbMzBtIHwgG1swbRtbMzNtbXlzdHJpbmcgICAgICAgICAgICAgICAgICAg\nICAgICAgIHN0ciAgICAgICAgICAgICAgICAgICAgICAgICAgICBoZWxsbyB3b3JsZAobWzBtICAg\nIBtbMzBtIHwgG1swbRtbOTZtbXl2YXIgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHN0ciAg\nICAgICAgICAgICAgICAgICAgICAgICAgICB0ZXN0X3ByaW50X29iamVjdF90YWJsZQobWzBtICAg\nIBtbMzBtIHwgG1swbRtbMzNtdmFyICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByb3Bl\ncnR5ICAgICAgICAgICAgICAgICAgICAgICAbWzk2bTc3G1swbQobWzBtICAgIBtbMzBtIHwgG1sw\nbRtbOTZtd29ybGQgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZ1bmN0aW9uChtbMG0bWzBt\n')

        res = console(foo, plaintext=True, retval=True)
        self.assert_equal_b64(

            res.replace("__main__", "tests"),
            b'PF9fbWFpbl9fLkZvb2JhciBvYmplY3Q+OiBGb29iYXIgY2xhc3MKG1s5MG0gfCBGb29iYXIgICAg\nICAgICAgICAgIHR5cGUgICAgICAgICAgICAgIHZhbHVlCnwgLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tCnwgX19wcml2YXRldmFyICAgICAgICAgICBpbnQgICAgICAgNzcKfCBoZWxs\nbyAgICAgICAgICAgICAgIGZ1bmN0aW9uCnwgbXlzdHJpbmcgICAgICAgICAgICAgc3RyICAgICAg\nIGhlbGxvIHdvcmxkCnwgbXl2YXIgICAgICAgICAgICAgICBzdHIgICAgICAgdGVzdF9wcmludF9v\nYmplY3RfdGFibGUKfCB2YXIgICAgICAgICAgICAgICAgcHJvcGVydHkgICAgNzcKfCB3b3JsZCAg\nICAgICAgICAgICAgIGZ1bmN0aW9uClswbQ==\n')
        self.assert_equal_b64(

            console(
                AA(),
                retval=True).replace("tests", "__main__"),
            b'MC4wMCB8IF9fbWFpbl9fLnB5OjMxNxtbMG0bWzMwbSB8IBtbMG0bWzBtG1szMG08X19tYWluX18u\nQUEgb2JqZWN0PjogG1szNG1BQSd0amUbWzBtCiAgICAbWzkxbSB8IEFBICAgICAgICAgICAgICAg\nICAgICAgICAgICAgICAgICB0eXBlICAgICAgICAgICAgICAgICAgICAgICAgICAgdmFsdWUbWzBt\nCiAgICAbWzMwbSB8IC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t\nLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLRtbMG0KICAgIBtb\nMzBtIHwgG1swbRtbMzNtZm9vICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGZ1bmN0aW9u\nChtbMG0gICAgG1szMG0gfCAbWzBtG1s5Nm1tX2Zsb2F0ICAgICAgICAgICAgICAgICAgICAgICAg\nICAgZmxvYXQgICAgICAgICAgICAgICAgICAgICAgICAgIBtbMzhtOC4wG1swbQobWzBtICAgIBtb\nMzBtIHwgG1swbRtbMzNtbV9pbnQgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGludCAgICAg\nICAgICAgICAgICAgICAgICAgICAgICAbWzk2bTgbWzBtChtbMG0gICAgG1szMG0gfCAbWzBtG1s5\nNm1tX3N0cmluZyAgICAgICAgICAgICAgICAgICAgICAgICAgc3RyICAgICAgICAgICAgICAgICAg\nICAgICAgICAgIGhlbGxvChtbMG0bWzBt\n')


class Foobar(object):
    """
    Foobar, testclass for printing an object
    """
    def __str__(self):
        """
        __str__
        """
        return "Foobar class"

    def __init__(self, myvar):
        """
        @type myvar: str
        @return: None
        """
        self.myvar = myvar
        self.__privatevar = 77
        self.mystring = "hello world"
        super().__init__()

    def hello(self):
        """
        hello
        """
        print(self.mystring)

    def world(self):
        """
        world
        """
        return self.__privatevar

    @property
    def var(self):
        """
        var
        """
        return self.__privatevar

    @var.setter
    def var(self, v):
        """
        @type v: str
        @return: None
        """
        self.__privatevar = v


def db64(b):
    """
    @type b: bytes
    @return: None
    """
    b = base64.decodebytes(b)
    s = b.decode("utf-8")
    return s


def gb64(s):
    """
    @type s: str
    @return: None
    """
    s = s.encode()
    bs = base64.encodebytes(s)
    return bs


def main():
    """
    main
    """
    unit_test_main(globals())

standard_library.install_aliases()


if __name__ == "__main__":
    main()
