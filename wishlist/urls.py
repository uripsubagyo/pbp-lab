from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_data_res
from wishlist.views import show_data_json
from wishlist.views import show_id_json
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax
from wishlist.views import add_barang


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_data_res, name='show_data_res'),
    path('json/', show_data_json, name='show_data_json'),
    path('json/<int:id>', show_id_json, name='show_id_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax , name='show_wishlist_ajax'),
    path('ajax/submit', add_barang, name='add_barang'),
]