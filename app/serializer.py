## we can include serializer in urls.py but is preferred to make another file for it.
## Serializer is used to convert to JSON File.

from rest_framework import serializers
from app.models import User

class User_Serializer(serializers.HyperlinkedModelSerializer):
    Identification_ID=serializers.ReadOnlyField()
    class Meta:
        model=User
        fields='__all__'    
        ## We can serialize all fields by using __all__ but limited fields being serialized helps minimize bandwidth usage and sent response of what client requires.

