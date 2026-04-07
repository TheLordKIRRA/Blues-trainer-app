Blues Trainer App — System Architecture

Overview
The system follows a three-tier architecture:

- Frontend (React)  
  Handles UI, form input, dashboards, and API calls.

- Backend (Flask)  
  Provides REST API endpoints, authentication, validation, 
  business logic (analytics, streaks), and DB operations.

- Database (PostgreSQL)  
  Stores users, practice sessions, statistics, and analytics data.

 Data Flow Diagram
1. User interacts with frontend
2. Frontend sends JSON requests to Flask API
3. Flask validates and processes data
4. Flask stores or retrieves data from PostgreSQL
5. Backend returns structured JSON responses for UI rendering

The system promotes:
- Low coupling  
- Single responsibility  
- Easy testability  
- Clear layering
  
