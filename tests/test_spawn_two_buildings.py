# :copyright (c) URBANopt, Alliance for Sustainable Energy, LLC, and other contributors.
# See also https://github.com/urbanopt/geojson-modelica-translator-examples/blob/develop/LICENSE.md

import shutil
from pathlib import Path
from unittest import TestCase

from geojson_modelica_translator.geojson_modelica_translator import GeoJsonModelicaTranslator

# from geojson_modelica_translator.modelica.modelica_runner import ModelicaRunner


class SpawnTwoBuildingTest(TestCase):
    def setUp(self):
        self.project_name = "spawn_geojson"
        self.data_dir = Path(__file__).parent.parent / "examples" / "spawn_two_buildings"
        self.output_dir = Path(__file__).parent.parent / "output"
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True, exist_ok=False)

        self.results_path = self.output_dir / self.project_name
        if self.results_path.exists():
            shutil.rmtree(self.results_path)

    def test_to_modelica_defaults(self):
        feature_json_file = self.data_dir / f"{self.project_name}.json"
        sys_params_json_file = self.data_dir / "spawn_system_params.json"

        gmt = GeoJsonModelicaTranslator(
            feature_json_file,
            sys_params_json_file,
            self.output_dir,
            self.project_name,
        )

        gmt.to_modelica()

        assert (
            self.results_path
            / "Loads"
            / "Resources"
            / "Data"
            / "B5a6b99ec37f4de7f94020090"
            / "RefBldgSmallOfficeNew2004_v1.4_9.6_5A_USA_IL_CHICAGO-OHARE.idf"
        )

        # test running just a Spawn coupling - no longer able to run with JModelica.
        # mr = ModelicaRunner()
        # file_to_run = self.results_path / "Loads" / 'B5a6b99ec37f4de7f94020090' / 'coupling.mo'

        # success, _ = mr.run_in_docker(file_to_run, run_path=self.output_dir, project_name=self.project_name)
        # self.assertTrue(success)

        # results_path = Path(self.output_dir / f"{self.project_name}_results")
        # self.assertTrue(Path(results_path) / 'stdout.log')
        # self.assertTrue(
        #     Path(results_path) / 'spawn_single_Loads_B5a6b99ec37f4de7f94020090_SpawnCouplingETS.fmu'
        # )
