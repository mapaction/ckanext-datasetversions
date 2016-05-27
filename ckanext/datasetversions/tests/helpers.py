import nose.tools

import ckan.tests.helpers as helpers
import ckan.plugins as plugins

assert_equals = nose.tools.assert_equals
assert_true = nose.tools.assert_true
assert_regexp_matches = nose.tools.assert_regexp_matches


class TestBase(helpers.FunctionalTestBase):
    @classmethod
    def setup_class(cls):
        super(TestBase, cls).setup_class()
        plugins.load('datasetversions')

    @classmethod
    def teardown_class(cls):
        plugins.unload('datasetversions')
        super(TestBase, cls).teardown_class()