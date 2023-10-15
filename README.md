<<<<<<< HEAD
0x00. AirBnB clone - The console


Group project
Python
OOP

https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231010T082828Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=01e5a49de87726218977145759b52273c168fb51373b9cf8331509e255b8ce84

Background Context
Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object


https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231010%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231010T082828Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a590dfc2f0d58c9f2c42e57e57598db9fc3fdb1623fb35ea0db63614baabcf16
=======
# 0x00. AirBnB clone - The console
## Background Context
First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

<ins>Each task is linked and will help you to:</ins>

  * put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
  * create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
   * create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
   * create the first abstracted storage engine of the project: File storage.
   * create all unittests to validate all our classes and storage engine
>>>>>>> e6ad1f5ea2cc4ee4b1502c204517c4611dfef174
