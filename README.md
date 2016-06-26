# Clean Architecture Implementation

### Simple Store.


#### Top-Bottom overview

- Web Controller (Flask):
  
  Only know about the user input and validating its own domain. Json, types of form, etc.

  So that he doesn't know about the lower level complexity of performing the operations, 
  the Use Cases are hidden behind a DepdencyInjector abstraction.
  
  He knows he asks for the specific use case manager to this depedency handler, and performs the
  desired operation on the outcome that the handler gives back.... Note that he needs to know what operation
  he wants to perform, so the point of the dependency handler is kind of weak... Need to look more into this.
  
  Also note that the controller needs to know what to look for in the response from the use case. This is 
  understandable, at the end of the day, he of course needs to know what to do and what to do with the returned
  values from said operation.
  
- Dependency Handler (Pure)
  
  The benefit of this handler is that hides away the lower level creation complexity, if the UseCase needs access
  to the Database implementations, a network resource, a filesystem to do its job, the upper layer doesn't need
  to know that, he just gives the object fully created and ready to do the action he demanded. There is value on this.

  That could possibly be a way to test in isolation a controller, you don't care how what you asked is created, or
  how it cames up with the values it gives you, you test what you do with those values. Again, this is weak, because
  in production, you DO care where that data came up.
  
  Unsure if the dependency handler is to be clasified as a boundary or a top level controller. More work needed on this.
  
- Managers (Pure + SQL + Requests + Memcached)

  This are the guys that the dependency handler builds. They perform the operation that the user requested. The operation
  most of the times requires logic being done and I/O, construct a new user and save it, do some calculation
  and store the result, pull certain info and do something, so this would be our application service,
  they use cases, create domain models, store their results in I/O and they take I/O and pass them to the use cases
  so that they can do something with them.
  
  Basically this it heart of the application. In here will be logic that filters stored data, which is really important, because
  lets say we wan't all users who have a pending payment. It won't be effective to pull all users from the database,
  and go through them in the logic, what happens when there are a bunch of them? Running all operations through the core logic is not
  viable.
  
  This should give to the uses cases the data in a form that they can understand, meaning either domain objects, or pure values.
  With that, these managers already have 3 responsabilities, call the use cases, store the results on I/O, call I/O to give the
  results to the uses cases, and convert the results from I/O format to domain format and viceversa. They are the most complicated
  piece on the whole system, and guess what, they are the less tested.
  
  They are looking less and less good to my eyes.

  This needs a whole more of work and thought to make sure is doable.
  
- Use Cases (Pure)

  This would be the classes that perform operations on the domain objects. They should receive IO from the upper class. So far nothing
  in here, cause I don't have any yet.
  
  They should receive domain objects or pure values.
  
- Domain objects (Pure)

  Lowest leve of objects in here. They represent business objects. They could be either values, or objects. For now I'm
  using objects cause they can have a certain low level rules, say how are they created, etc. That could be done with an
  UseCase and a simple value object, but I think I like it better this way.
  
  There is not that many complexity here. Easy to unit test, all the relationships here should be with other Domain objects
  or simply values.
