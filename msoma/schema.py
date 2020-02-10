import graphene
import graphql_jwt

import catalog.schema


class Query(catalog.schema.Query, graphene.ObjectType):
    pass


class Mutation(catalog.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)