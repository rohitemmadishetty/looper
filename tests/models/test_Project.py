""" Tests for the NGS Project model. """

import os
from looper.models import Project


__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"



class ProjectRequirementsTests:
    """ Tests for a Project's set of requirements. """


    def test_minimal_configuration_doesnt_fail(
            self, minimal_project_conf_path):
        """ Project construction requires nothing """
        Project(config_file=minimal_project_conf_path)


    def test_minimal_configuration_name_inference(
            self, tmpdir, minimal_project_conf_path):
        project = Project(minimal_project_conf_path)
        _, expected_name = os.path.split(tmpdir.strpath)
        assert expected_name == project.name


    def test_minimal_configuration_output_dir(
            self, tmpdir, minimal_project_conf_path):
        project = Project(minimal_project_conf_path)
        assert tmpdir.strpath == project.output_dir
