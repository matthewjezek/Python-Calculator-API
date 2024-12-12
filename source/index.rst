.. Python-Calculator-API documentation master file, created by
   sphinx-quickstart on Thu Dec 12 10:00:56 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python-Calculator-API's documentation!
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. plantuml::

   @startuml
   actor User
   User -> API : Request /add
   API -> Calculator : Perform addition
   Calculator -> API : Return result
   API -> User : Return response
   @enduml

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
