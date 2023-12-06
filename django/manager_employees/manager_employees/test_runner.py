from django.test.runner import DiscoverRunner


class CustomTestRunner(DiscoverRunner):
    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        test_labels += ('tests.login_test',)
        return super().build_suite(test_labels, extra_tests, **kwargs)
