# Copyright (c) 2009, Rackspace.
# See COPYING for details.

"""
Flavor Manager - entity manager for Cloud Servers flavors.
"""

from cloudservers.entitymanager import EntityManager
from cloudservers.entitylist import EntityList
from cloudservers.errors import BadMethodFault, NotImplementedException
from cloudservers.flavor import Flavor

"""
BadMethodFault is raised whenever a method is called that is not allowed.

Because flavors are immutable (provided by the API) and can not be changed
through the API.
"""
_bmf = BadMethodFault("FlavorManager")

class FlavorManager(EntityManager):
    """
    Manages the list of server Flavors
    """
    def __init__(self, cloudServersService):
        super(FlavorManager, self).__init__(cloudServersService, "flavors")

    def create(self, entity):
        raise _bmf
    def create(self, entity):
        raise _bmf
    def refresh(self, entity):
        raise _bmf
    def remove(self, entity):
        raise _bmf

    #
    # Polling Operations
    #
    def wait (self, entity):
        raise _bmf

    def waitT (self, entity, timeout):
        raise _bmf

    def notify (self, entity, changeListener):
        raise _bmf

    def stopNotify (self, entity, changeListener):
        raise _bmf

    def createEntityListFromResponse(self, response, detail):
        """
        Creates list of Flavor objects from response to list command sent
        to API
        """
        # print response
        theList = []
        data = response["flavors"]
        for jsonObj in data:
            f = Flavor("")
            f.initFromResultDict(jsonObj)
            theList.append(f)

        return EntityList(theList, detail, self)
