from rest_framework import serializers  # type: ignore
from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

    def validate(self, data):
        # Validate that the product belongs to the specified organization
        product = data.get('product')

        # If org_id is null, we should not raise an error
        if product:
            if product.org_id is not None and hasattr(self.context, 'org_id'):
                org_id = self.context.get('org_id')

                if product.org_id != org_id:
                    raise serializers.ValidationError(
                        "The product does not belong to "
                        "the specified organization."
                    )

        return data
