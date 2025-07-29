@echo off
echo Running Simple Round 1B: Persona-Driven Analysis...
docker run --rm -v "D:/hackathon_adobe/app/input:/app/input" -v "D:/hackathon_adobe/app/output:/app/output" pdf-trainer python app/round1b/simple_round1b.py
echo.
echo Simple Round 1B completed!
pause 