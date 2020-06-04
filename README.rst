GeoJSON to Modelica Translator Examples
---------------------------------------

.. image:: https://travis-ci.org/urbanopt/geojson-modelica-translator.svg?branch=develop
    :target: https://travis-ci.org/urbanopt/geojson-modelica-translator

.. image:: https://coveralls.io/repos/github/urbanopt/geojson-modelica-translator/badge.svg?branch=develop
    :target: https://coveralls.io/github/urbanopt/geojson-modelica-translator?branch=develop


Description
-----------

To be completed

Getting Started
---------------

To run the tests in this repo execute the following in a terminal.

.. code-block:: bash

    pip install requests==2.22.0
    pip install -r requirements.txt

    py.test

Matrix of Examples to Create
----------------------------

+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| ID        | Number of Buildings | Building Loads | ETS Model | Network Model | District Plant                     | Status      |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 1 | 13                  | TEASER         | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | Complete    |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 2 | 13                  | Spawn          | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | In-progress |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 3 | 13                  | Timeseries     | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | -           |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+
| 4GDHC - 4 | 13                  | Mix            | Indirect  | 4-Pipe        | Chiller, Cooling Tower, and Boiler | -           |
+-----------+---------------------+----------------+-----------+---------------+------------------------------------+-------------+


Todos
-----

* handle weather!
* How to update git dependencies using pip
