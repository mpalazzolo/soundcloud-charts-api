Welcome to soundcloud-charts-api's documentation!
=================================================

A python wrapper for the Soundcloud Charts API.

**NOTE:** This is a wrapper for a public, undocumented API.

Dependencies
^^^^^^^^^^^^

* `Requests <https://github.com/requests/requests>`_

Installation
^^^^^^^^^^^^
::

    python setup.py install

or::

    pip install soundcloud-charts-api

Example
^^^^^^^
::

   from soundcloudcharts import SoundCloudCharts

   sc = SoundCloudCharts()
   chart_data = sc.get_chart(region='us', limit=10)

   for i, item in enumerate(chart_data['collection']):
      print('{0}: {1} - {2}'.format(str(i+1),
                                    item['track']['user']['username'],
                                    item['track']['title']))

API Parameters
^^^^^^^^^^^^^^
KIND:

* top
* trending (New & Hot)

GENRE:

* all-music
* all-audio
* alternativerock
* ambient
* classical
* country
* danceedm
* dancehall
* deephouse
* disco
* drumbass
* dubstep
* electronic
* folksingersongwriter
* hiphoprap
* house
* indie
* jazzblues
* latin
* metal
* piano
* pop
* rbsoul
* reggae
* reggaeton
* rock
* soundtrack
* techno
* trance
* trap
* triphop
* world

REGION:

* au (Australia)
* ca (Canada)
* fr (France)
* de (Germany)
* ie (Ireland)
* nl (Netherlands)
* nz (New Zealand)
* gb (Great Britain)
* us (United States)

:mod:`client` Module
^^^^^^^^^^^^^^^^^^^^

.. automodule:: soundcloudcharts.client
    :members:
    :special-members: __init__


:mod:`api_base` Module
^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: soundcloudcharts.api_base
    :members:
    :special-members: __init__


.. toctree::
   :maxdepth: 2
   :caption: Contents:

Versioning
^^^^^^^^^^

v1.0.1 - Initial Release - 08/18/2019
v1.0.2 - Fixed bug when using proxies - 08/19/2019
v1.0.3 - Updated file where key is found - 01/01/2020
v1.0.4 - Update to automatically find file with key - 03/09/2020

Authors
^^^^^^^

* **Matt Palazzolo** - `GitHub Profile <https://github.com/mpalazzolo>`_

License
^^^^^^^
https://github.com/mpalazzolo/soundcloud-charts-api/LICENSE.txt

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
