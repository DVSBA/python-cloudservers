# Copyright (c) 2009, Rackspace.
# See COPYING for details.


"""
Entity is the base class for all objects managed by EntityManagers.
"""

class Entity(object):
    """
    Entity object; base class of all Entities managed by EntityManagers.
    """
    def __init__(self, name=""):
        self._name = name
        self._id = None

    @property
    def id(self):
        """
        Get the Entity's id"""
        return self._id

    @property
    def name(self):
        """
        Get the Entity's name
        """
        return self._name

    def __repr__(self):
        """
        Get the cononical representation of the object, in this case,
        all vars in the object in string form
        """
        return str(vars(self))

    def __eq__(self, other):
        """
        eq assumes that if all the values in the lhs are the same as
        all the equivalent values on the rhs, then they're the same.
        obviously, if there are more attrs on the lhs, they're ignored
        but this serves our purpose
        """
        try:
            for v in vars(self):
                if getattr(self,v) != getattr(other,v):
                    return False
        except AttributeError:
            return False
        return True
