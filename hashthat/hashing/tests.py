from .forms import HashForm
from .models import Hash
from django.test import TestCase
from selenium import webdriver
import hashlib

TEST_STRING = "hello"
TEST_HASH = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"


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
        string = TEST_STRING
        hash = TEST_HASH
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
        form = HashForm(data={"text": TEST_STRING})
        self.assertTrue(form.is_valid())

    def test_hash_func_works(self):
        text_hash = hashlib.sha256(TEST_STRING.encode("utf-8")).hexdigest()
        self.assertEqual(text_hash, TEST_HASH, "Hash function does not work")

    def save_hash(self):
        hash = Hash()
        hash.text = TEST_STRING
        hash.hash = TEST_HASH
        hash.save()
        return hash

    def test_hash_object(self):
        hash = self.save_hash()
        pulled_hash = Hash.objects.get(hash=TEST_HASH)
        self.assertEqual(hash.text, pulled_hash.text)

    def test_viewing_hash(self):
        hash = self.save_hash()
        response = self.client.get(f"/hash/{hash.hash}")
        self.assertContains(response, TEST_STRING)
