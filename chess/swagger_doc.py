from drf_yasg.views import get_schema_view
from drf_yasg import openapi

doc_schema = get_schema_view(
    openapi.Info(
        title="The Chess Daemon",
        default_version="v1",
        description="Documentation of chess.d APIs",
        contact=openapi.Contact(
            email="sathvic.p@gmail.com", name="Sathvic Pushpakaran"
        ),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)