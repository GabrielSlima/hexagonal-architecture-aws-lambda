# hexagonal-architecture-aws-lambda

## Concepts from hexagonal architecture
- Adapters: these are how external components interacts with the application, or how the application interacts with external systems or other application components
- Entrypoints: handles inboud requests made to the application. They are the inbound adapters
- Services: encapsulates application level business logic
- Domain: encapsulates busines objects
- Inbound ports defines the operations the application have, aligns with business logic
- Outboud ports defines how the application communicate with external systems and components

## concept and patterns from DDD
Aggregates, entities, value objects, policies, services and 
