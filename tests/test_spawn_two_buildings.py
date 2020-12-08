"""
****************************************************************************************************
:copyright (c) 2019-2020 URBANopt, Alliance for Sustainable Energy, LLC, and other contributors.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions
and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the
distribution.

Neither the name of the copyright holder nor the names of its contributors may be used to endorse
or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
****************************************************************************************************
"""

import shutil
from pathlib import Path
from unittest import TestCase

from geojson_modelica_translator.geojson_modelica_translator import (
    GeoJsonModelicaTranslator
)
from geojson_modelica_translator.modelica.modelica_runner import ModelicaRunner
from geojson_modelica_translator.system_parameters.system_parameters import (
    SystemParameters
)


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

        gj = GeoJsonModelicaTranslator.from_geojson(feature_json_file)
        sys_params_json_file = self.data_dir / 'spawn_system_params.json'
        gj.set_system_parameters(SystemParameters(sys_params_json_file))
        gj.process_loads()

        self.assertEqual(len(gj.loads), 2)
        gj.to_modelica(self.project_name, self.output_dir)

        self.assertTrue(self.results_path / "Loads" / "Resources" / "Data" / "B5a6b99ec37f4de7f94020090" / "RefBldgSmallOfficeNew2004_Chicago.idf")  # noqa

        mr = ModelicaRunner()
        file_to_run = Path(gj.scaffold.loads_path.files_dir) / 'B5a6b99ec37f4de7f94020090' / 'coupling.mo'
        run_path = Path(gj.scaffold.project_path).parent

        exitcode = mr.run_in_docker(file_to_run, run_path=run_path, project_name=gj.scaffold.project_name)
        self.assertEqual(0, exitcode)

        results_path = Path(run_path / f"{gj.scaffold.project_name}_results")
        self.assertTrue(Path(results_path) / 'stdout.log')
        self.assertTrue(
            Path(results_path) / 'spawn_single_Loads_B5a6b99ec37f4de7f94020090_SpawnCouplingETS.fmu'
        )
