"""Project schema"""

import graphene

from movies.schema import Query as MovieQuery, Mutation as MovieMutation


class Query(MovieQuery, graphene.ObjectType):
    """Query object type"""
    ping = graphene.String()

    def resolve_ping(root, info):
        return "Pong!"


class Mutation(MovieMutation, graphene.ObjectType):
    """Mutation object type"""


schema = graphene.Schema(query=Query, mutation=Mutation)