from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Friend, Memory
from .forms import MeetingForm


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def friends_index(request):
    friends = Friend.objects.all()
    return render(request, 'friends/index.html', {'friends': friends})


def friends_detail(request, friend_id):
    friend = Friend.objects.get(id=friend_id)
    memories_not_assoc_w_friend = Memory.objects.exclude(
        id__in=friend.memories.all().values_list('id'))
    meeting_form = MeetingForm()
    return render(request, 'friends/detail.html', {
        'friend': friend, 'meeting_form': meeting_form,
        'memories': memories_not_assoc_w_friend
    })


class FriendCreate(CreateView):
    model = Friend
    fields = ['name', 'ethnicity', 'height', 'age']
    succes_url = '/friends/'


class FriendUpdate(UpdateView):
    model = Friend
    fields = ['ethnicity', 'height', 'age']


class FriendDelete(DeleteView):
    model = Friend
    success_url = '/friends/'


def add_meeting(request, friend_id):
    form = MeetingForm(request.POST)
    if form.is_valid():
        new_meeting = form.save(commit=False)
        new_meeting.friend_id = friend_id
        new_meeting.save()
    return redirect('detail', friend_id=friend_id)


def assoc_memory(request, friend_id, memory_id):
    Friend.objects.get(id=friend_id).memories.add(memory_id)
    return redirect('detail', friend_id=friend_id)


class MemoryList(ListView):
    model = Memory


class MemoryDetail(DetailView):
    model = Memory


class MemoryCreate(CreateView):
    model = Memory
    fields = '__all__'


class MemoryUpdate(UpdateView):
    model = Memory
    fields = ['name', 'description', 'year']


class MemoryDelete(DeleteView):
    model = Memory
    success_url = '/memories/'
