# File: views.py
# Author: Justin Wang (justin1@bu.edu), 4/3/2025
# Description: Views

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Voter
import plotly
import plotly.graph_objs as go
from django.db.models import Count

# Create your views here.

class VotersListView(ListView):
    """View to display voters"""

    template_name = 'voters.html'
    model = Voter
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        """Get the queryset for the voters"""
        results = super().get_queryset()
        
        if self.request.GET.get('party_affiliation'):
            results = results.filter(party_affiliation=self.request.GET.get('party_affiliation'))
        
        if self.request.GET.get('min_birth_year'):
            results = results.filter(date_of_birth__year__gte=self.request.GET.get('min_birth_year'))
            
        if self.request.GET.get('max_birth_year'):
            results = results.filter(date_of_birth__year__lte=self.request.GET.get('max_birth_year'))

        if self.request.GET.get('voter_score'):
            results = results.filter(voter_score=self.request.GET.get('voter_score'))

        if self.request.GET.get('v20state'):
            results = results.filter(v20state='TRUE')
            
        if self.request.GET.get('v21primary'):
            results = results.filter(v21primary='TRUE')
            
        if self.request.GET.get('v22general'):
            results = results.filter(v22general='TRUE')
            
        if self.request.GET.get('v21town'):
            results = results.filter(v21town='TRUE')
            
        if self.request.GET.get('v23town'):
            results = results.filter(v23town='TRUE')

        return results

    def get_context_data(self, **kwargs):
        """Add additional context data"""
        context = super().get_context_data(**kwargs)
        
        # Get min and max years
        years = Voter.objects.dates('date_of_birth', 'year')
        min_year = years.first().year
        max_year = years.last().year
        
        context['party_choices'] = Voter.objects.values_list('party_affiliation', flat=True).distinct()
        context['birth_years'] = range(min_year, max_year + 1)
        context['voter_score'] = Voter.objects.values_list('voter_score', flat=True).distinct().order_by('voter_score')
        context['v20state'] = Voter.objects.values_list('v20state', flat=True).distinct()
        context['v21primary'] = Voter.objects.values_list('v21primary', flat=True).distinct()
        context['v22general'] = Voter.objects.values_list('v22general', flat=True).distinct()
        context['v21town'] = Voter.objects.values_list('v21town', flat=True).distinct()
        context['v23town'] = Voter.objects.values_list('v23town', flat=True).distinct()
        
        return context

class VoterDetailView(DetailView):
    """View to display a single voter's details"""
    template_name = 'voter_detail.html'
    model = Voter
    context_object_name = 'voter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voter = self.get_object()
        address = f"{voter.residential_street_number}+{voter.residential_street_name}"
        if voter.residential_apartment_number:
            address += f"+Apartment+{voter.residential_apartment_number}"
        address += f",+{voter.residential_zip_code}"
        context['google_maps_url'] = f"https://www.google.com/maps/search/?api=1&query={address}"
        return context

class GraphsView(ListView):
    """View to display graphs of voter data"""
    template_name = 'graphs.html'
    model = Voter
    context_object_name = 'voters'

    def get_queryset(self):
        """Get the queryset for the voters, applying any filters"""
        results = super().get_queryset()
        
        if self.request.GET.get('party_affiliation'):
            results = results.filter(party_affiliation=self.request.GET.get('party_affiliation'))
        
        if self.request.GET.get('min_birth_year'):
            results = results.filter(date_of_birth__year__gte=self.request.GET.get('min_birth_year'))
            
        if self.request.GET.get('max_birth_year'):
            results = results.filter(date_of_birth__year__lte=self.request.GET.get('max_birth_year'))

        if self.request.GET.get('voter_score'):
            results = results.filter(voter_score=self.request.GET.get('voter_score'))

        if self.request.GET.get('v20state'):
            results = results.filter(v20state='TRUE')
            
        if self.request.GET.get('v21primary'):
            results = results.filter(v21primary='TRUE')
            
        if self.request.GET.get('v22general'):
            results = results.filter(v22general='TRUE')
            
        if self.request.GET.get('v21town'):
            results = results.filter(v21town='TRUE')
            
        if self.request.GET.get('v23town'):
            results = results.filter(v23town='TRUE')

        return results

    def get_context_data(self, **kwargs):
        """Add additional context data including the graphs"""
        context = super().get_context_data(**kwargs)
        
        # Get min and max years
        years = Voter.objects.dates('date_of_birth', 'year')
        min_year = years.first().year
        max_year = years.last().year
        
        context['party_choices'] = Voter.objects.values_list('party_affiliation', flat=True).distinct()
        context['birth_years'] = range(min_year, max_year + 1)
        context['voter_score'] = Voter.objects.values_list('voter_score', flat=True).distinct().order_by('voter_score')
        context['v20state'] = Voter.objects.values_list('v20state', flat=True).distinct()
        context['v21primary'] = Voter.objects.values_list('v21primary', flat=True).distinct()
        context['v22general'] = Voter.objects.values_list('v22general', flat=True).distinct()
        context['v21town'] = Voter.objects.values_list('v21town', flat=True).distinct()
        context['v23town'] = Voter.objects.values_list('v23town', flat=True).distinct()
        
        # Get filtered queryset
        voters_queryset = self.get_queryset()
        
        # Birth year histogram
        birth_years_data = voters_queryset.values('date_of_birth__year').annotate(
            count=Count('id')).order_by('date_of_birth__year')
        
        x_birth_years = [entry['date_of_birth__year'] for entry in birth_years_data]
        y_birth_counts = [entry['count'] for entry in birth_years_data]
        
        fig_birth_years = go.Bar(x=x_birth_years, y=y_birth_counts)
        voter_count = voters_queryset.count()
        title_text = f"Voter distribution by Year of Birth (n={voter_count})"
        graph_div_birth_years = plotly.offline.plot(
            {"data": [fig_birth_years], "layout": {"title": title_text}},
            auto_open=False,
            output_type="div"
        )
        context['graph_div_birth_years'] = graph_div_birth_years
        
        # Party affiliation pie chart
        party_data = voters_queryset.values('party_affiliation').annotate(
            count=Count('id')).order_by('-count')
        
        party_labels = [entry['party_affiliation'] for entry in party_data]
        party_counts = [entry['count'] for entry in party_data]
        
        fig_party = go.Pie(labels=party_labels, values=party_counts)
        title_text = f"Voter distribution by Party Affiliation (n={voter_count})"
        graph_div_party = plotly.offline.plot(
            {"data": [fig_party], "layout": {"title": title_text}},
            auto_open=False,
            output_type="div"
        )
        context['graph_div_party'] = graph_div_party
        
        # Election participation histogram
        elections = [
            {'field': 'v20state', 'label': '2020 State'},
            {'field': 'v21town', 'label': '2021 Town'},
            {'field': 'v21primary', 'label': '2021 Primary'},
            {'field': 'v22general', 'label': '2022 General'},
            {'field': 'v23town', 'label': '2023 Town'}
        ]
        
        election_labels = [election['label'] for election in elections]
        election_counts = []
        
        for election in elections:
            count = voters_queryset.filter(**{election['field']: 'TRUE'}).count()
            election_counts.append(count)
        
        fig_elections = go.Bar(x=election_labels, y=election_counts)
        title_text = f"Vote Count by Election (n={voter_count})"
        graph_div_elections = plotly.offline.plot(
            {"data": [fig_elections], "layout": {"title": title_text}},
            auto_open=False,
            output_type="div"
        )
        context['graph_div_elections'] = graph_div_elections
        
        return context