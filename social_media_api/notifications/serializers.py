class NotificationSerializer(serializers.ModelSerializer):
    actor = UserSerializer(read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target', 'read', 'timestamp']  # updated
        read_only_fields = ['id', 'timestamp']  # updated