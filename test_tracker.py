import unittest
from tracker_logic import add_application, update_status, get_application

class TestJobTracker(unittest.TestCase):

    def setUp(self):
        # This runs before every single test - gives us a fresh list eeach time
        self.apps = []

    def test_add_application(self):
        result = add_application(self.apps, "Google", "SWE Intern", "03/02/2026")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["company"], "Google")
        self.assertEqual(result[0]["role"], "SWE Intern")
        self.assertEqual(result[0]["status"], "Applied")

    def test_add_mulitple_applications(self):
        add_application(self.apps, "Google", "SWE Intern", "03/02/2026")
        add_application(self.apps, "Dematic", "Java Intern", "03/03/2026")
        self.assertEqual(len(self.apps), 2)

    def test_update_status(self):
        add_application(self.apps, "Proofpoint", "SE Intern", "03/02/2026")
        result = update_status(self.apps, 0, "Interview")
        self.assertEqual(result[0]["status"], "Interview")

    def test_update_invalid_index(self):
        add_application(self.apps, "Trimble", "SE Intern", "03/02/2026")
        result = update_status(self.apps, 99, "Interview")
        self.assertIsNone(result)

    def test_get_applications(self):
        add_application(self.apps, "CGI", "Dev Intern", "03/02/2026")
        app = get_application(self.apps, 0)
        self.assertEqual(app["company"], "CGI")

    def test_get_invalid_infex(self):
        result=get_application(self.apps, 0)
        self.assertIsNone(result)

    if __name__ == "__main__":
        unittest.main()