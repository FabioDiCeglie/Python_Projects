from django.urls import path
from restapi.views import ExpenseListCreate, ExpenseRetrieveDelete

urlpatterns = [
    path("expenses/", ExpenseListCreate.as_view(), name="expense-list-create"),
    path(
        "expenses/<pk>",
        ExpenseRetrieveDelete.as_view(),
        name="expense-retrieve-delete",
    ),
]
