from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from rest_framework.views import APIView

from .models import Person, SportClub, Tournament, Results
from .serializers import PersonSerializer, SportClubSerializer, TournamentSerializer, ResultsSerializer


# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = {
        'PersonList': '/person_list',
        'Person_details': '/person_detail/:id',
        'SportClubList': '/sport_club_list',
        'SportClub_details': '/sport_club_detail/:id',
        'TournamentList': '/tournament_list',
        'Tournament_details': '/tournament_detail/:id',
        'ResultList': '/results_list',
        'Result_details': '/results_detail/:id',
    }
    return Response(data)


# @api_view(['GET','POST'])
# def person_list(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#
#         if query == None:
#             query = ''
#
#         persons = Person.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
#         serializer = PersonSerializer(persons, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         person = Person.objects.create(
#             name=request.data['name'],
#             surname=request.data['surname']
#         )
#
#         serializer = PersonSerializer(person, many=False)
#
#         return Response(serializer.data)

class PersonList(APIView):

    def get_object(self, query):
        try:
            return Person.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
        except Person.DoesNotExist:
            raise JsonResponse('Person doesnot exist', safe=False)

    def get(self, request):
        query = request.GET.get('query')

        if query == None:
            query = ''
        persons = self.get_object(query)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        person = Person.objects.create(
            name=request.data['name'],
            surname=request.data['surname'],
            role=request.data['role'],
            born_year=request.data['born_year'],
            sport_club=request.data['sport_club']
        )
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)


class PersonDetail(APIView):

    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except Person.DoesNotExist:
            raise JsonResponse('Person doesnot exist', safe=False)

    def get(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        person = self.get_object(id)
        person.name = request.data['name']
        person.surname = request.data['surname']
        # person.role = request.data['role']
        # person.born_year = request.data['born_year']
        # person.sport_club = request.data['sport_club']
        person.save()
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        person = self.get_object(id)
        person.delete()
        return Response('User was deleted')


# inna metoda podobno nieco gorsza
# @api_view(['GET', "PUT", "DELETE"])
# def person_detail(request, id):
#     person = Person.objects.get(id=id)
#
#     if request.method == "GET":
#         serializer = PersonSerializer(person, many=False)
#         return Response(serializer.data)
#
#     if request.method == "PUT":
#         person.name = request.data['name']
#         person.surname = request.data['surname']
#
#         person.save()
#         serializer = PersonSerializer(person, many=False)
#         return Response(serializer.data)
#
#     if request.method == "DELETE":
#         person.delete()
#         return Response('User was deleted')
# @api_view(['GET'])
# def sport_clubs_list(request):
#     query = request.GET.get('query')
#
#     if query == None:
#         query = ''
#
#     clubs = SportClub.objects.filter(Q(country__icontains=query) | Q(name__icontains=query))
#     serializer = SportClubSerializer(clubs, many=True)
#     return Response(serializer.data)

class SportClubsList(APIView):

    def get_object(self, query):
        try:
            return SportClub.objects.filter(Q(name__icontains=query) | Q(country__icontains=query))
        except SportClub.DoesNotExist:
            raise JsonResponse('Sport club does not exist')

    def get(self, request):
        query = request.GET.get('query')

        if query == None:
            query = ''
        sportclub = self.get_object(query)
        serializer = SportClubSerializer(sportclub, many=True)
        return Response(serializer.data)

    def post(self, request):
        sportclub = SportClub.objects.create(
            name=request.data['name'],
            country=request.data['country']
        )
        serializer = SportClubSerializer(sportclub, many=False)
        return Response(serializer.data)


class SportClubDetail(APIView):

    def get_object(self, id):
        try:
            return SportClub.objects.get(id=id)
        except SportClub.DoesNotExist:
            raise JsonResponse('SportClub doesnot exist', safe=False)

    def get(self, request, id):
        sportclub = self.get_object(id)
        serializer = SportClubSerializer(sportclub, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        sportclub = self.get_object(id)
        sportclub.name = request.data['name']
        sportclub.country = request.data['country']
        sportclub.save()
        serializer = SportClubSerializer(sportclub, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        sportclub = self.get_object(id)
        sportclub.delete()
        return Response('Sport club was deleted')

class TournamentsList(APIView):

    def get_object(self, query):
        try:
            return Tournament.objects.filter(Q(name__icontains=query))
        except Tournament.DoesNotExist:
            raise JsonResponse('Tournament club does not exist')

    def get(self, request):
        query = request.GET.get('query')

        if query == None:
            query = ''
        tournament = self.get_object(query)
        serializer = TournamentSerializer(tournament, many=True)
        return Response(serializer.data)

    def post(self, request):
        tournament = Tournament.objects.create(
            name=request.data['name'],
            organizator=request.data['organizator'],
            rank=request.data['rank'],
            rank_point=request.data['rank_point'],
            year=request.data['year']
        )
        serializer = TournamentSerializer(tournament, many=False)
        return Response(serializer.data)


class TournamentDetail(APIView):

    def get_object(self, id):
        try:
            return Tournament.objects.get(id=id)
        except Tournament.DoesNotExist:
            raise JsonResponse('Tournament does not exist', safe=False)

    def get(self, request, id):
        tournament = self.get_object(id)
        serializer = TournamentSerializer(tournament, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        tournament = self.get_object(id)
        tournament.name = request.data['name']
        tournament.organizator = request.data['organizator']
        tournament.rank = request.data['rank']
        tournament.rank_point = request.data['rank_point']
        tournament.year = request.data['year']
        tournament.save()
        serializer = TournamentSerializer(tournament, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        tournament = self.get_object(id)
        tournament.delete()
        return Response('tournament club was deleted')

class ResultList(APIView):

    def get_object(self, query):
        try:
            return Results.objects.filter(Q(place__icontains=query) | Q(category_age__icontains=query) | Q(category_weight__icontains=query))
        except Results.DoesNotExist:
            raise JsonResponse('Result club does not exist')

    def get(self, request):
        query = request.GET.get('query')

        if query == None:
            query = ''
        results = self.get_object(query)
        serializer = ResultsSerializer(results, many=True)
        return Response(serializer.data)

    def post(self, request):
        results = Results.objects.create(
            place=request.data['place'],
            participant=request.data['participant'],
            tournament=request.data['tournament'],
            category_age=request.data['category_age'],
            category_weight=request.data['category_weight']
        )
        serializer = ResultsSerializer(results, many=False)
        return Response(serializer.data)


class ResultClubDetail(APIView):

    def get_object(self, id):
        try:
            return Results.objects.get(id=id)
        except Results.DoesNotExist:
            raise JsonResponse('Result does not exist', safe=False)

    def get(self, request, id):
        results = self.get_object(id)
        serializer = ResultsSerializer(results, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        results = self.get_object(id)
        results.place = request.data['place']
        results.participant = request.data['participant']
        results.tournament = request.data['tournament']
        results.category_age = request.data['category_age']
        results.category_weight = request.data['category_weight']
        serializer = ResultsSerializer(results, many=False)
        return Response(serializer.data)

    def delete(self, request, id):
        results = self.get_object(id)
        results.delete()
        return Response('Result was deleted')
