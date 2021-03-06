xmldirector.dropbox
===================

Integration of 

- Plone (https://www.plone.org)
- XML Director (https://www.xml-director.info) 
- Dropbox

Requirements
------------

- Plone 4.3 (tested)
  
- Plone 5.0 (tested)

- XML Director 2.0 (xmldirector.plonecore)


Usage
-----

First you need to register your own App as Dropbox developer
on https://dropbox.com/developer. Your application must be configured
for full dropbox access. The application key and application secret
must be configured globally inside your Plone site setup -> XML Director
Dropbox setting.

A ``Connector`` instance must be authorized with Dropbox (see ``Dropbox``
tab/action).

The connection URL for a ``Connector`` connected to Dropbox must be
``dropbox://dropbox.com/``.


License
-------
This package is published under the GNU Public License V2 (GPL 2)

Source code
-----------
See https://github.com/xml-director/xmldirector.dropbox

Bugtracker
----------
See https://github.com/xml-director/xmldirector.dropbox


Author
------
| Andreas Jung/ZOPYX
| Hundskapfklinge 33
| D-72074 Tuebingen, Germany
| info@zopyx.com
| www.zopyx.com

