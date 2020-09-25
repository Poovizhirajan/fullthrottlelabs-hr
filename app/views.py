from django.http import JsonResponse
from app.models import User, ActivityPeriod
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def fetch_user_records(request):
    """

    Fetching all the user records.

    Parameters: No parameter

    Result: Json format

    """
    if request.method == "GET":
        user_obj = User.objects.values()
        activity_period_obj = ActivityPeriod.objects.values("start_time", "end_time")
        list_result = [data for data in user_obj]
        list_result1 = [data1 for data1 in activity_period_obj]
        return JsonResponse({"ok": True, "members": list_result, "activity_periods": list_result1})
