from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard
from bson import ObjectId

# Helper to convert ObjectId to string
def objectid_to_str(obj):
    return str(obj) if isinstance(obj, ObjectId) else obj

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']
    def get_id(self, obj):
        return objectid_to_str(obj.id)

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'is_superhero']
    def get_id(self, obj):
        return objectid_to_str(obj.id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'date']
    def get_id(self, obj):
        return objectid_to_str(obj.id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    suggested_for_team = TeamSerializer(read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for_team']
    def get_id(self, obj):
        return objectid_to_str(obj.id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'total_points']
    def get_id(self, obj):
        return objectid_to_str(obj.id)
