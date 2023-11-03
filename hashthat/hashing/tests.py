from .forms import HashForm
from django.test import TestCase
from selenium import webdriver
import hashlib


class FunctionalTestCase(TestCase):
    pass

    """
    def setUp(self):
        # ? https://www.geeksforgeeks.org/how-to-install-selenium-in-python/
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_there_is_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("install", self.browser.page_source)

    def test_hash_of_hello(self):
        string = "hello"
        hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        self.browser.get("http://localhost:8000")
        text = self.browser.find_element_by_id("text")
        text.send_keys(string)
        self.browser.find_element_by_name("submit").click()
        self.assertIn(hash, self.browser.page_source)
    """


class UnitTestCase(TestCase):
    def test_home_homepage_tempalte(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "hashing/home.html")

    def test_hash_form(self):
        form = HashForm(data={"text": "hello"})
        self.assertTrue(form.is_valid())

    def test_hash_func_works(self, text_to_hash="hello"):
        check = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        text_hash = hashlib.sha256("hello".encode("utf-8")).hexdigest()
        self.assertEqual(text_hash, check, "Hash function does not work")
