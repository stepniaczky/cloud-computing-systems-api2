import strawberry
from permissions import IsAdmin

@strawberry.type
class Query:
    @strawberry.field(permission_classes=[IsAdmin])
    def hello(self, info, name: str = "World") -> str:
        return f"Hello {name}!"
    
    @strawberry.field
    def goodbye(self, info, name: str = "World") -> str:
        return f"Goodbye {name}!"
    
    