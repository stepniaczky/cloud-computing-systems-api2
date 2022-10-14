import strawberry
import azure.functions as func
import nest_asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from schema import Query

nest_asyncio.apply()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://turbo-barber-api.azurewebsites.net"],
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema=schema, graphiql=True)
app.include_router(graphql_app, prefix="/graphql")


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)
