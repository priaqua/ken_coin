#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from Src.TestBase.WebDriverSetup import Util


class TestDemo:

    @pytest.fixture
    def test_setup(self):
        return 1

    def test_first(self):
        print("hello, ")
        print(Util.total(2, 3))
        print(" people")


