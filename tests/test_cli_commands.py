import shutil
from pathlib import Path
from unittest import TestCase

from click.testing import CliRunner

# from geojson_modelica_translator.geojson_modelica_translator import (
#     GeoJsonModelicaTranslator
# )
# from geojson_modelica_translator.uo_des import cli

# Integration tests that the CLI works as expected for an end user


class CLIIntegrationTest(TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.data_dir = Path(__file__).parent.parent / 'examples' / 'dhc' / 'spawn'
        self.output_dir = Path(__file__).parent.parent / 'examples' / 'dhc' / 'spawn' / 'output'

    def test_cli_spawn_district(self):
        # In python 3.8 we can drop the if statement and simplify this to "my_file.unlink(missing_ok=True)"
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)

        self.output_dir.mkdir(exist_ok=True)

        # run subprocess as if we're an end-user
        res = self.runner.invoke(
            'uo_des',
            [
                'create-model',
                str(self.data_dir / 'spawn_system_params_ex1.json'),
                str(self.data_dir / 'spawn_geojson_ex1.json'),
                str(self.output_dir / 'junk-mcjunk-face'),
                '--overwrite'
            ]
        )

        assert res.exit_code == 0

        # If this file exists, the cli command ran successfully
        assert (self.output_dir / 'test_sys_param.json').exists()

        # If this file exists, the cli command ran successfully
        assert (self.output_dir / 'modelica_project' / 'Districts' / 'DistrictEnergySystem.mo').exists()

        # Now run the model
        self.runner.invoke(
            'uo_des',
            [
                'run-model',
                str(self.output_dir / 'modelica_project')
            ]
        )

        # If this file exists, the cli command ran successfully
        assert (self.output_dir / 'modelica_project_results' / 'modelica_project_Districts_DistrictEnergySystem_result.mat').exists()
