from django.urls import path, include
from users.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AggregateCount

app_name = 'api'

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # users
    path('users/', include('users.urls', namespace='users')),

    # grants
    path('grants/', include('grants.urls', namespace='grants')),

    # events
    path('events/', include('events.urls', namespace='events')),

    # proposals
    path('proposals/', include('proposals.urls', namespace='proposals')),

    # consultancies
    path('consultancies/', include('consultancies.urls', namespace='consultancies')),

    # workshops
    path('workshops/', include('workshops.urls', namespace='workshops')),

    # lectures
    path('lectures/', include('lectures.urls', namespace='lectures')),

    # talks
    path('talks/', include('talks.urls', namespace='talks')),

    # achievements
    path('achievements/', include('achievements.urls', namespace='achievements')),

    # conferences
    path('conferences/', include('conferences.urls', namespace='conferences')),

    # patents
    path('patents/', include('patents.urls', namespace='patents')),

    # activities
    path('activities/', include('activities.urls',
                                namespace='activities')),

    # books
    path('books/', include('books.urls',
                           namespace='books')),

    # industrial_visits
    path('industrial_visits/', include('industrial_visits.urls',
                                       namespace='industrial_visits')),

    # mous
    path('mous/', include('mous.urls',
                          namespace='mous')),

    # memberships
    path('memberships/', include('memberships.urls',
                                 namespace='memberships')),

    # for chart data
    path('aggregate/', AggregateCount.as_view(), name='listcount')
]
