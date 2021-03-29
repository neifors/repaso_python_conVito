""" Contains helpers to accumulate iterable class attributes.
"""
from collections.abc import Mapping
from functools import partial
from itertools import chain


class Accumulate:
    """ Inherit iterable class attributes, accumulating values along the way.

        Implements a descriptor over iterable types that chains the current and parent
        class values together. Values are only retrieved from immediate parents, but
        Accumulate can be used repeatedly at multiple inheritance levels to provide deep
        retrieval.

        Supports Mapping types (including defaultdict) Top level key collisions prefer
        the child-most value. If the mapping is ordered, the result will be ordered, but
        note that collisions will maintain the original position.

        Note: These operations can be considered "shallow" - only top level values are
        accumulated. For mappings, that means Container *values* will be replaced, not
        merged.

        >>> class Base:
        ...     fields = ("id",)
        ...     metadata = {"filter_fields": ("id",), "read_only_field": ("id",)}
        ...
        >>> class User(Base):
        ...     fields = accumulate(("name", "password"))
        ...     metadata = accumulate({
        ...         "filter_fields": ("name",),
        ...         "invisible_fields": ("password",)
        ...     })
        ...
        >>> User.fields
        ('name', 'password', 'id')
        >>> User.metadata
        {'filter_fields': ('name',), 'read_only_field': ('id',), 'invisible_fields': ('password',)}
    """

    def __init__(self, values):
        self.constructor = type(values)
        # Support constructors with factories, such as defaultdict
        if hasattr(values, "default_factory"):
            self.constructor = partial(self.constructor, values.default_factory)
        self.is_mapping = isinstance(values, Mapping)
        self.name = None
        self.values = values

    def __get__(self, obj, type_):
        if type_ is None:
            type_ = type(obj)
        if self.name is None:
            self._infer_name(type_)
        # Prefer object local values from __set__
        if obj is not None and self.name in obj.__dict__:
            return obj.__dict__[self.name]
        collection = (
            iterable
            for iterable in chain(
                [self.values],
                (getattr(base, self.name, None) for base in type_.__bases__),
            )
            if iterable
        )
        if self.is_mapping:
            # Reverse the order of mappings to be parent->leaf to prefer leaf values
            collection = (d.items() for d in reversed(tuple(collection)))
        return self.constructor(chain.from_iterable(collection))

    def __set__(self, obj, values):
        if self.name is None:
            self._infer_name(type(obj))
        obj.__dict__[self.name] = values

    def __set_name__(self, type_, name):
        """ Set the field name during class initialization on py3.6+. See `_infer_name` for cases where this is not
            called.
        """
        self.name = name

    def _infer_name(self, type_):
        """ Infer a field name for py3.5- or when the descriptor is added with setattr (which won't call __set_name__).
        """
        all_attributes = chain.from_iterable(dir(cls) for cls in type_.__mro__)
        attributes = {attr for attr in all_attributes if not attr.startswith("__")}
        for attr in attributes:
            if type_.__dict__[attr] is self:
                self.name = attr
        if self.name is None:
            raise ValueError("Unable to determine attribute name on {}.".format(type_))


accumulate = Accumulate
