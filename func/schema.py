import strawberry

@strawberry.type
class Query:
    @strawberry.field
    def hello(self, info, name: str = "World") -> str:
        return f"Hello {name}!"
    
    @strawberry.field
    def goodbye(self, info, name: str = "World") -> str:
        return f"Goodbye {name}!"
    
    