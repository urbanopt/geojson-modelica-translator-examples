GeoJSON to Modelica Translator Examples
---------------------------------------

.. image:: https://travis-ci.org/urbanopt/geojson-modelica-translator-examples.svg?branch=develop
    :target: https://travis-ci.org/urbanopt/geojson-modelica-translator-examples

.. image:: https://coveralls.io/repos/github/urbanopt/geojson-modelica-translator-examples/badge.svg?branch=develop
    :target: https://coveralls.io/github/urbanopt/geojson-modelica-translator-examples?branch=develop


Description
-----------

To be completed

Getting Started
---------------

To run the tests in this repo execute the following in a terminal.

.. code-block:: bash

    pip install requests==2.24.0
    pip install -r requirements.txt

    py.test

Note to update git pip packages then run:

.. code-block:: bash

    pip install -U --upgrade-strategy eager -r requirements.txt


Matrix of Examples to Create
----------------------------

+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| ID        | Number of Buildings | Building Loads | ETS Model | Network Model | District Plant                     | Status      |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 1 | 8                   | TEASER         | N/A       | N/A           | Infinite Heating and Cooling       | Complete    |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 2 | 2                   | Spawn          | N/A       | N/A           | Infinite Heating and Cooling       | Complete    |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 3 | 8                   | TEASER         | Indirect  | None          | Infinite Heating and Cooling       | In-progress |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 4 | 2                   | Spawn          | Indirect  | None          | Infinite Heating and Cooling       | In-progress |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 5 | TBD                 | Time Series    | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | -           |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 6 | 8                   | Mix            | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | -           |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+


Todos
-----

* handle weather!
