from rest_framework import (  # type: ignore
    serializers
)


class OrganisationSerializer(serializers.ModelSerializer):
    fields = '__all__'
    read_only_fields = [
        'id',
        'created_at',
        'updated_at',
    ]
