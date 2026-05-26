"""Pages views."""
from django.shortcuts import render
from django.views.generic import TemplateView


class About(TemplateView):
    """View for the about page."""

    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        """Return context with page title."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'О проекте'
        return context


class Rules(TemplateView):
    """View for the rules page."""

    template_name = 'pages/rules.html'

    def get_context_data(self, **kwargs):
        """Return context with page title."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Наши правила'
        return context


def page_not_found(request, exception):
    """Render 404 page."""
    return render(request, 'pages/404.html', status=404)


def server_error(request):
    """Render 500 page."""
    return render(request, 'pages/500.html', status=500)


def csrf_failure(request, reason=''):
    """Render 403 CSRF failure page."""
    return render(request, 'pages/403csrf.html', status=403)
