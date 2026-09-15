"""
GraphQL schema for NetBox Software Plugin.

For more information on NetBox GraphQL, see:
https://docs.netbox.dev/en/stable/plugins/development/graphql/

For Strawberry GraphQL documentation, see:
https://strawberry.rocks/
"""

from typing import List

import strawberry
import strawberry_django

from .models import Netboxsoftware


@strawberry_django.type(
    Netboxsoftware,
    fields='__all__',
)
class NetboxsoftwareType:
    """GraphQL type for Netboxsoftware model."""
    pass


@strawberry.type(name="Query")
class NetboxsoftwareQuery:
    """GraphQL queries for NetBox Software Plugin."""

    netboxsoftware: NetboxsoftwareType = strawberry_django.field()
    netboxsoftware_list: List[NetboxsoftwareType] = strawberry_django.field()


schema = [
    NetboxsoftwareQuery,
]

