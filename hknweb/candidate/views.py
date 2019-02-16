from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .models import OffChallenge

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'candidate/index.html'

class CandRequestView(CreateView, generic.ListView):
    template_name = 'candidate/candreq.html'
    model = OffChallenge
    fields = ['name', 'officer', 'description', 'proof']
    success_url = "/cand/candreq"

    context_object_name = 'challenge_list'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.requester = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CandRequestView, self).get_context_data(**kwargs)
        # context['search_field'] = CandRequestView.search_field
        # context['status'] = CandRequestView.status
        return context

    def get_queryset(self):
        result = OffChallenge.objects

        result = result.order_by('-request_date')
        return result

def challenge_detail_view(request, pk):
    challenge = OffChallenge.objects.filter(id=pk).values()[0]
    return render(request, "candidate/challenge_detail.html", challenge)
