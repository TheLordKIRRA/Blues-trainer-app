Milestone 2: Design and Implementation Progress

System Architecture & Design:

The Blues Trainer App follows a modular client-server architecture designed to support scalability, maintainability, and clear separation of concerns. The frontend communicates with a Flask-based backend through RESTful API endpoints, which handle authentication, session management, and analytics requests. The backend is structured into organized layers including routes, services, models, and schemas to ensure that business logic, data handling, and validation remain independent and easy to maintain. The database layer uses MySQL managed through SQLAlchemy ORM, allowing structured interaction with persistent data such as users and practice sessions. Authentication is handled using secure password hashing and token-based session management. This architecture was chosen to allow incremental expansion into analytics, audio processing, and machine learning features without restructuring the core system.


[ Frontend (React / UI) ]
            |
            v
[ Flask API Layer (Routes) ]
            |
            v
[ Service Layer (Business Logic) ]
            |
            v
[ SQLAlchemy ORM Models ]
            |
            v
[ MySQL Database ]


Front-End Development:

The front-end development has focused on establishing a functional and user-friendly interface aligned with the application’s goals. A basic dashboard layout has been implemented to display user information, recent practice sessions, and summary statistics. Forms for user registration and login have been created, allowing interaction with backend authentication endpoints. The UI structure prioritizes clarity and simplicity so users can easily log sessions and view progress without confusion. While styling and responsiveness are still being refined, the current implementation supports core user flows including account creation, login, and viewing stored data. The design decisions emphasize usability and future integration of data visualization tools such as charts and performance graphs.

Back-End & Database:

The backend implementation includes a fully structured Flask application with working API endpoints for user registration, authentication, and practice session management. SQLAlchemy models define the database schema, including tables for users and practice sessions with appropriate relationships and constraints. Passwords are securely stored using hashing functions, ensuring user data protection. The database connection has been configured using MySQL, with attention given to resolving connection issues such as port configuration errors. Core CRUD operations for practice sessions are functional, allowing users to create, retrieve, update, and delete session data. The backend is designed to support future expansion into analytics processing and audio-based performance evaluation without major restructuring.

Version Control & Collaboration:

Version control has been maintained through consistent use of GitHub, with commits reflecting incremental progress across backend setup, database configuration, frontend development, and in-person collaboration. Responsibilities have been clearly divided between system design and implementation, allowing parallel progress while maintaining alignment with the overall product vision. Collaboration has focused on ensuring that architectural decisions match implementation feasibility, reducing the risk of misalignment between planned features and working code. Communication between roles has supported steady development progress, with updates and fixes applied as issues such as database connectivity were identified and resolved. Along with new problems to be addressed in the final processes such as proper app initialization.
