from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ('title', 'body', 'completed')

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none() # needed

    # get_queryset = lambda self: PersonalNote.objects.filter(user=self.request.user) # won't fully work
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return self.queryset # OR return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)