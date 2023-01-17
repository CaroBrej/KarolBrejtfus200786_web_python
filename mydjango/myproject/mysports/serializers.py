from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Person, SportClub, Tournament, Results


class SportClubSerializer(ModelSerializer):
    members_count = SerializerMethodField(read_only=True)
    class Meta:
        model = SportClub
        fields = '__all__' #['','']

    def get_members_count(self, obj):
        count = obj.person_set.count()
        return count


class TournamentSerializer(ModelSerializer):
    organizator = SportClubSerializer()
    class Meta:
        model = Tournament
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    sport_club = SportClubSerializer()
    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'role', 'born_year', 'sport_club']


class ResultsSerializer(ModelSerializer):
    participant = PersonSerializer()
    tournament = TournamentSerializer()
    class Meta:
        model = Results
        fields = '__all__'