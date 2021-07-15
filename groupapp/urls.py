from django.urls import path
from . import views
from profiles.views import signUP,LoginUser,profiles,logout_user,EditProfile,changePassword,changeName
from posts.views import createPost_ajax,seePosts,postFromYou,delete


urlpatterns = [
    path('signup/',signUP,name='signup'),
    path('login/',LoginUser,name='login'),
    path('',views.index,name="index"),
    path('profiles/',profiles,name="profiles"),
    path('logout/',logout_user,name="logout"),
    path('profiles/EditProfile/',EditProfile,name="EditProfile"),
    path('profiles/EditProfile/changePassword',changePassword,name="changePassword"),
    path('profiles/EditProfile/Change_name',changeName,name="changename"),

    #  for groups
    path('creategroup/',views.creategroup,name="creategroup"),
    path('Allgroups/',views.AllGroups,name="groups"),
    # ajax Groups
    path('Allgroups/join/',views.join_ajax,name="join_ajax"),
    path('Allgroups/delete/',views.delete_ajax,name="delete_ajax"),

    # POSts 
    path('posts_ajax/<int:id>',createPost_ajax,name="createPost_ajax"),
    path('seePosts/<int:id>',seePosts,name="seePosts"),
    path('postFromYou/',postFromYou,name="postFromYou"),

    # Posts Ajax
    path('delete/', delete,name=" delete"),

   




]
