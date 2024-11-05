from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Teams:
    name: str
    des: str
    members: List[str]

teams: Dict[str, Teams] = {
    "procurement": Teams(
        name="Procurement",
        des="Procurement: We buy food to cook so that we can feed you guys at lunch time and we buy supplies like soap, trash bags, etc.",
        members=["Jacob", "Markel", "Aaron", "Arthur"]
    ),
    "management": Teams(
        name="Management",
        des="""Management Team:
    As the Management team we are required to manage all of the chores for each day and who does them.
    This includes:
    Cleaning the kitchen, and taking out the trash.
    Sweeping the main lobby and also sweeping the back hallway/classrooms.
    Wiping all the tables, including the kitchen tables.""",
        members=["Chris", "Kilan", "Aidan", "Tanner"]
    ),
    "documentation": Teams(
        name="Documentation",
        des="Documentation team is responsible for taking photos of guest speakers, community events, and unit projects. After taking the pictures, depending on the event happening in the photos, we determine which social media to post on. We are also responsible for getting all the photos for the yearbook.",
        members=["Jason", "Patrick"]
    ),
    "community": Teams(
        name="Community",
        des="Community: Our job is to plan events that bring people together, build lasting relationships, and promote engagement.",
        members=["Arianna", "Peyton"]
    ),
}

def bcca_team_view(request: HttpRequest, team_name: str = None) -> HttpResponse:
    if team_name:
        team = teams.get(team_name)
        if team is None:
            return HttpResponse("Team not found", status=404)
        return render(request, "home.html", {'team': team})

    return render(request, "home.html", {'teams': list(teams.keys())})


