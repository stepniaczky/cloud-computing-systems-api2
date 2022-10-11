import graphene
import azure.functions as func
import nest_asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from schema import Query

nest_asyncio.apply()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://turbo-barber-api.azurewebsites.net"],
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = graphene.Schema(query=Query)
app.add_route("/api", GraphQLApp(schema=schema,
              on_get=make_graphiql_handler()))


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    # return func.AsgiMiddleware(app).handle(req, context)
    return func.HttpResponse("Hello World")
