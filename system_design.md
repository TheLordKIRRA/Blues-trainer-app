System Design

Technical Solutions:
Techinical solutions to the project requirements would be things such as utilizing Python/Django for user sign in/sign up, utilizing APIs that have been built specialized for music apps, utilizing HTML, CSS, and Javascript for app design and functionality for frontend UI, utilizing the wide availability of possible references to look up and help us as we progress and run into forseen or possibly previously solved problems. 
System Architecture:
System will have SQL based local storage for record keeping, this is where the users accuracy score is recorded in order to display play accuracy progression along with temporary storage of played user input for accuracy analysis. Play accuracy progression will be handled by an API "User Progress & Analytics" which will allow the user to see their progress accross practice sessions. The system will utilize more specialized APIs in order to detect notes' tone, tune, and tempo. The system will perform an accuracy to inteded played music through "Audio Looping & Backing Track" API which will take the recorded user input and compare it to hardcoded practice music and display accuracy along with an accuracy breakdown based off tune, tone, and tempo. 
Choose technologies and data structures:
Technologies that we will utilize for the project are the programming languages SQL, HTML, CSS, Javascript, and Python, along with the following APIs: (Audio processing API, Machine Learning, Fretboard Visualization API, Music Theory API, Metronome & Tempo Control API, Tuner API, User Progress & Analytics API).
SQL: The language that will be utilized for data storage locally within the app for temporary user input data and accuracy scores tied to play sessions data
HTML: Language that will be utilized for app base structure and layout 
CSS: language that will be utilized for app design and fine details
Javascript: language that will be utilized for accessing functions and activating functions of the apps program
Python/Django: language that will be utilized for the machine learning, along with being the base for user sign in and signup
Audio processing API: To analyze the user’s playing in real time, this API detects pitch, timing, and note accuracy. It enables features like chord recognition, strumming pattern analysis, and feedback on finger placement.
Machine Learning: Powers advanced features such as pitch recognition and chord identification.
Fretboard Visualization API: Renders interactive fretboards that display finger positions, note locations, and chord diagrams. This helps users visualize and internalize patterns across the neck.
Music Theory API: Provides access to chord and scale databases, interval training, and theoretical guidance. It supports features like identifying the correct note in a given key.
Metronome & Tempo Control API: Offers precise timing and tempo adjustments, often with customizable beats and time signatures, to help users practice rhythm and timing.
Tuner API: Uses the device’s microphone to detect pitch and guide tuning, often with visual feedback (e.g., needle or color indicators) for standard and alternate tunings.
User Progress & Analytics API: Tracks user performance over time—such as accuracy, speed, and completion of lessons—enabling personalized learning paths and progress visualization.
Diagrams and Design Documents:
