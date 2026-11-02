from .models import Organization, MetricPayload

def get_unprocessed_org_metrics():
    # Using select_related for 1-to-many/foreign key joins (SQL INNER/LEFT JOIN)
    # Using prefetch_related for reverse foreign keys / many-to-many
    return Organization.objects.prefetch_related(
        models.Prefetch(
            'metrics',
            queryset=MetricPayload.objects.filter(processed=False).order_by('-created_at')
        )
    ).all()